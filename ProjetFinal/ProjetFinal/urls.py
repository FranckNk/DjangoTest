"""ProjetFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
    curl -d "title='Bonjour'&Valeur=20" http://127.0.0.1:8000/arduino
    
    curl -H "Content-Type: application/json" -X POST -d '{"nom":Bonjour,"val":20}' http://127.0.0.1:8000/arduino > result.html
    curl -X POST http://127.0.0.1:8000/arduino -H 'Content-Type: application/json' -d '{"nom":Bonjour,"val":20}'
curl -X POST http://127.0.0.1:8000/arduino -H "Content-Type: application/x-www-form-urlencoded" -d "nom='Bonjour'&val=20"
curl -X POST http://192.168.1.112:8000/arduino -H "Content-Type: application/x-www-form-urlencoded" -d "nom='slaut'&val=40"

netsh interface portproxy add v4tov4 listenport=8000 connectaddress=192.168.1.112 listenaddress=127.0.0.1
    
    
"""
from django.contrib import admin
from django.urls import path, include
from ArduinoServer import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.DonneeViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'arduino', views.arduino_list),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
 