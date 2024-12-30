"""
URL configuration for ofe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from ui_service import views
from images_management_service.api.viewsets import ImageFournisseurViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/images-fournisseur', ImageFournisseurViewSet, basename='imagefournisseur')


urlpatterns = [
    # Default
    path('', views.index, name='index'),

    #Admin
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # Activation de l’authentification fournie par DRF pour nous connecter
    path('admin/', admin.site.urls),
    
    # Web
    path('404/', views.error_404, name='404'),
    path('blank/', views.blank, name='blank'),
    path('buttons/', views.buttons, name='buttons'),
    path('cards/', views.cards, name='cards'),
    path('charts/', views.charts, name='charts'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('tables/', views.tables, name='tables'),
    path('utilities-animation/', views.utilities_animation, name='utilities-animation'),
    path('utilities-border/', views.utilities_border, name='utilities-border'),
    path('utilities-color/', views.utilities_color, name='utilities-color'),
    path('utilities-other/', views.utilities_other, name='utilities-other'),

    # Photothèque
    path('phototheque/refresh/', views.phototheque_refresh, name='phototheque-refresh'),
    path('phototheque/history/', views.phototheque_history, name='phototheque-history'),
    path('phototheque/admin/', views.phototheque_admin, name='phototheque-admin'),
    
    # Visuels fournisseur
    path('visuels-fournisseur/create-package/', views.visuels_fournisseur_create_package, name='visuels-fournisseur-create-package'),
    path('visuels-fournisseur/associate/', views.visuels_fournisseur_associate, name='visuels-fournisseur-associate'),
    path('visuels-fournisseur/transform/', views.visuels_fournisseur_transform, name='visuels-fournisseur-transform'),
]

urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

urlpatterns += router.urls
