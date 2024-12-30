from rest_framework.serializers import ModelSerializer
 
from images_management_service.models.imagefournisseur import ImageFournisseur
 
class ImageFournisseurSerializer(ModelSerializer):

    class Meta:
        model = ImageFournisseur
        fields = ['name','url','supplier_name','width', 'height']