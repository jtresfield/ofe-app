from django.contrib import admin
from django.apps.registry import apps

from images_management_service.models import Image

# Enregistrement de tous les modèles des apps pour les rendre accessibles dans l'IHM admin Django
admin.site.register(apps.all_models['data_importation_service'].values())
admin.site.register(apps.all_models['data_transformation_service'].values())
admin.site.register(apps.all_models['data_validation_service'].values())
admin.site.register(apps.all_models['images_management_service'].values())
admin.site.register(apps.all_models['ui_service'].values())