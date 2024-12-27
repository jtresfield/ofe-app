from rest_framework.views import APIView
from rest_framework.response import Response
 
from images_management_service.models import Image
from images_management_service.api.serializers import ImageSerializer
 
class ImageAPIView(APIView):
 
    def get(self, *args, **kwargs):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)