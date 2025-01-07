from rest_framework.viewsets import ModelViewSet
 
from images_management_service.models.imagefournisseur import ImageFournisseur
from images_management_service.api.serializers import ImageFournisseurSerializer
from images_management_service.models.imageimport import ImageImport
from images_management_service.api.serializers import ImageImportSerializer
 
class ImageFournisseurViewSet(ModelViewSet):

    """
    ViewSet pour gérer les opérations CRUD de la table ImageFournisseur.
    """
    queryset = ImageFournisseur.objects.all()
    serializer_class = ImageFournisseurSerializer

class ImageImportViewSet(ModelViewSet):

    """
    ViewSet pour gérer les opérations CRUD de la table ImageImport.
    """
    # image_import = ImageImport.objects.get(id=1)
    # testt = image_import.images.all()
    queryset = ImageImport.objects.all()
    serializer_class = ImageImportSerializer

class ImageConvertViewSet(ModelViewSet):
    """
    ViewSet pour convertir des fichiers EPS en JPG.
    """
    queryset = ImageFournisseur.objects.all()
    serializer_class = ImageFournisseurSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        if instance.url.name.endswith('.eps'):
            instance.convert_eps_to_jpg()
            # Sauvegarder après conversion
            instance.save()