from django.shortcuts import render
from ui_service.api_config import API_ENDPOINTS
import requests


# Create your views here.

def index(request):
    return render(request, 'index.html')

def old_index(request):
    return render(request, 'bootstrap-templates/old-index.html')

def error_404(request):
    return render(request, 'bootstrap-templates/404.html')

def blank(request):
    return render(request, 'bootstrap-templates/blank.html')

def buttons(request):
    return render(request, 'bootstrap-templates/buttons.html')

def cards(request):
    return render(request, 'bootstrap-templates/cards.html')

def charts(request):
    return render(request, 'bootstrap-templates/charts.html')

def forgot_password(request):
    return render(request, 'bootstrap-templates/forgot-password.html')

def login(request):
    return render(request, 'bootstrap-templates/login.html')

def register(request):
    return render(request, 'bootstrap-templates/register.html')

def tables(request):
    return render(request, 'bootstrap-templates/tables.html')

def utilities_animation(request):
    return render(request, 'bootstrap-templates/utilities-animation.html')

def utilities_border(request):
    return render(request, 'bootstrap-templates/utilities-border.html')

def utilities_color(request):
    return render(request, 'bootstrap-templates/utilities-color.html')

def utilities_other(request):
    return render(request, 'bootstrap-templates/utilities-other.html')


# Photothèque
def phototheque_refresh(request):
    return render(request, 'phototheque/phototheque-refresh.html')

def phototheque_history(request):
    return render(request, 'phototheque/phototheque-history.html')

def phototheque_admin(request):
    return render(request, 'phototheque/phototheque-admin.html')


# Visuels fournisseur
def visuels_fournisseur_import(request):
    """
    Vue pour afficher la liste des images packages via l'API.
    """
    response = requests.get(API_ENDPOINTS['image_import'])  # URL dynamique si nécessaire
    if response.status_code == 200:
        imports = response.json()  # Les données renvoyées par l'API
    else:
        imports = []  # Par défaut, liste vide en cas d'erreur
    return render(request, 'visuels-fournisseur/visuels-fournisseur-import.html', {'imports': imports})

def visuels_fournisseur_associate(request):
    """
    Vue pour afficher la liste des images fournisseur via l'API.
    """
    response = requests.get(API_ENDPOINTS['image_fournisseur'])  # URL dynamique si nécessaire
    if response.status_code == 200:
        images = response.json()  # Les données renvoyées par l'API
    else:
        images = []  # Par défaut, liste vide en cas d'erreur
    return render(request, 'visuels-fournisseur/visuels-fournisseur-associate.html', {'images': images})

def visuels_fournisseur_transform(request):
    return render(request, 'visuels-fournisseur/visuels-fournisseur-transform.html')