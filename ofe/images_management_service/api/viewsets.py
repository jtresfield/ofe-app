from rest_framework.viewsets import ModelViewSet
 
from images_management_service.models.imagefournisseur import ImageFournisseur
from images_management_service.api.serializers import ImageFournisseurSerializer
 
class ImageFournisseurViewSet(ModelViewSet):

    """
    ViewSet pour gérer les opérations CRUD de la table ImageFournisseur.
    """
    queryset = ImageFournisseur.objects.all()
    serializer_class = ImageFournisseurSerializer