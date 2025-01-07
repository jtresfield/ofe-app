import os
from django.db import models
from django.dispatch import receiver
from PIL import Image
from django.db.models.signals import pre_save
from django.conf import settings  # Pour accéder à MEDIA_ROOT

from images_management_service.models.imageimport import ImageImport


# Images
class ImageFournisseur(models.Model):
    name = models.CharField(max_length=200, default='undefined')
    url = models.ImageField(upload_to='uploads/images/')
    supplier_name = models.CharField(max_length=50)
    width = models.CharField(max_length=10, default='undefined')
    height = models.CharField(max_length=10, default='undefined')
    image_import = models.ForeignKey(ImageImport, null=True, on_delete=models.SET_NULL)

    # Attribut temporaire pour éviter la récursion infinie
    _converted = False

    def __str__(self):
        return f'{self.name}'
    
    def convert_eps_to_jpg(self):
        """Convert EPS file to JPG using Pillow."""
        if self.url.name.endswith('.eps') and not self._converted:
            try:
                print(f"Attempting to convert {self.url.name} to JPG...")

                # Marquer comme converti pour éviter la boucle infinie
                self._converted = True

                # Remonter d'un cran pour accéder au dossier 'ghostscript'
                base_path = os.path.dirname(os.path.dirname(__file__))  # Remonte d'un niveau
                ghostscript_path = os.path.join(base_path, 'ghostscript', 'App')  # Dossier où Ghostscript est installé

                # Configurer les variables d'environnement pour Ghostscript
                os.environ['GS_LIB'] = os.path.join(ghostscript_path, 'lib')
                os.environ['PATH'] = os.path.join(ghostscript_path, 'bin') + os.pathsep + os.environ['PATH']

                # Si l'instance n'a pas encore de PK (ID), elle est nouvelle, donc sauvegarde-la d'abord
                if not self.pk:
                    self.save()

                # Ouvrir le fichier EPS avec Pillow
                img = Image.open(self.url)
                
                # Créer un chemin correct pour le fichier JPG, en utilisant MEDIA_ROOT
                jpg_filename = os.path.splitext(self.url.name)[0] + '.jpg'  # Génère le nom de fichier JPG
                jpg_path = os.path.join(settings.MEDIA_ROOT, jpg_filename)  # Utilise MEDIA_ROOT pour la sauvegarde

                # Convertir en JPG et sauvegarder
                img.convert('RGB').save(jpg_path, 'JPEG')

                # Mettre à jour l'URL de l'image avec le nouveau fichier JPG
                self.url.name = os.path.relpath(jpg_path, settings.MEDIA_ROOT)  # Met à jour le nom relatif du fichier
                
                # Enregistrer l'instance après la conversion
                if self.pk:  # Si l'instance a une clé primaire, mettre à jour l'URL uniquement
                    self.save(update_fields=['url'])
                else:  # Si l'instance n'a pas encore de pk, sauvegarder la nouvelle instance
                    self.save()

                print(f"Conversion réussie : {jpg_path}")

            except Exception as e:
                print(f"Erreur lors de la conversion : {e}")


# Signal pour calculer la taille de l'image avant de la sauvegarder
@receiver(pre_save, sender=ImageFournisseur)
def set_image_attributes(sender, instance, **kwargs):
    # Extraire le nom du fichier de l'URL
    instance.name = os.path.basename(instance.url.name)

    # Ouvrir l'image pour obtenir ses dimensions      
    if instance.url and instance.url.file:# Vérifier que l'image existe
        # Vérifier et convertir l'image si nécessaire
        if instance.url.name.endswith('.eps'):
            instance.convert_eps_to_jpg()
        
        img = Image.open(instance.url)
        instance.width = str(img.width)
        instance.height = str(img.height)