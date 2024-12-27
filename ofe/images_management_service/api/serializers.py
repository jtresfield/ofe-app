from rest_framework.serializers import ModelSerializer
 
from images_management_service.models import Image
 
class ImageSerializer(ModelSerializer):
 
    class Meta:
        model = Image
        fields = ['name']