from django.db import models

# Import d'images
class ImagePackage(models.Model):
    name = models.fields.CharField(max_length=200)
    creation_date = models.fields.DateField(auto_now_add=True)

    # String renvoyée par défaut de l'objet
    def __str__(self):
        return f'{self.name}'