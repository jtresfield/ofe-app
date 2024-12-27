from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.fields.CharField(max_length=200)

    # String renvoyée par défaut de l'objet
    def __str__(self):
        return f'{self.name}'