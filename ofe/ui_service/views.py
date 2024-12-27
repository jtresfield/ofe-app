from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

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