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