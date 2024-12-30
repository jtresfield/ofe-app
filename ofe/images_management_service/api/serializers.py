from rest_framework.serializers import ModelSerializer
 
from images_management_service.models.imagefournisseur import ImageFournisseur
from images_management_service.models.imageimport import ImageImport
 
class ImageFournisseurSerializer(ModelSerializer):

    class Meta:
        model = ImageFournisseur
        fields = ['name','url','supplier_name','width', 'height']

class ImageImportSerializer(ModelSerializer):

    class Meta:
        model = ImageImport
        fields = ['name']