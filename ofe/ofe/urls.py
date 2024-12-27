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
from django.contrib import admin
from rest_framework  import routers
from django.urls import include, path
from ui_service import views
from images_management_service.api.apiviews import ImageAPIView

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

    # API
    path('api/image/', ImageAPIView.as_view()),
]
