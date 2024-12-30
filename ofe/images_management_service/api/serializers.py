from rest_framework.serializers import ModelSerializer
 
from images_management_service.models.imagefournisseur import ImageFournisseur
from images_management_service.models.imagepackage import ImagePackage
 
class ImageFournisseurSerializer(ModelSerializer):

    class Meta:
        model = ImageFournisseur
        fields = ['name','url','supplier_name','width', 'height']

class ImagePackageSerializer(ModelSerializer):

    class Meta:
        model = ImagePackage
        fields = ['name']