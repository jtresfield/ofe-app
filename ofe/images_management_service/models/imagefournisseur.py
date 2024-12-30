import os
from django.db import models
from django.dispatch import receiver
from PIL import Image
from django.db.models.signals import pre_save

from images_management_service.models.imagepackage import ImagePackage


# Images
class ImageFournisseur(models.Model):
    name = models.CharField(max_length=200, default='undefined')
    url = models.ImageField(upload_to='uploads/images/')
    supplier_name = models.CharField(max_length=50)
    width = models.CharField(max_length=10, default='undefined')
    height = models.CharField(max_length=10, default='undefined')
    image_package = models.ForeignKey(ImagePackage, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


# Signal pour calculer la taille de l'image avant de la sauvegarder
@receiver(pre_save, sender=ImageFournisseur)
def set_image_attributes(sender, instance, **kwargs):
    # Extraire le nom du fichier de l'URL
    instance.name = os.path.basename(instance.url.name)

    # Ouvrir l'image pour obtenir ses dimensions
    if instance.url and instance.url.file:  # Vérifier que l'image existe
        img = Image.open(instance.url)
        instance.width = str(img.width)
        instance.height = str(img.height)
