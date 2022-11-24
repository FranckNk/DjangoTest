from pickletools import read_uint1
from django.http import HttpResponse
from django.shortcuts import render
from listeur.models import *
import requests
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from listeur.serializers import *

# Create your views here.


class ViewsBands(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Band.objects.all()
    serializer_class = BandsViews
    permission_classes = [permissions.IsAuthenticated]

class ViewsListeurs(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Listeur.objects.all()
    serializer_class = ListeurViews
    permission_classes = [permissions.IsAuthenticated]


def test(request):
    return HttpResponse(
        "<!DOCTYPE html><html><head><title>Tableau HTML</title><style>p, ul, li, h1{font-display: center ;background-color: cadetblue;border-radius: 20px;}</style></head><body class='BodyDesign'><p class='Paragraph'><h1><u>Un premier paragraphe.</u></h1><br> <!-- Et voici des commentaires en HTML--><br> <!-- Cette balise permet de faier un saut de ligne.--><i>Ici ce trouve un texte en italique.</i><b>Et par la suite un texte en gras.</b></p><ul>Et voici une liste non ordonnee en HTML.<li>Premier element.</li><li>Deuxieme element.</li></ul><br></body></html>"
    )

def band(request):
    bands = Band.objects.all()
    page = """\
        <h1>Hello Django !</h1>
        <p>Mes groupes Noms des Bands sont :<p>
        <ul>"""
    for a in bands:
        page = page + "<li>" + a.name + "</li>"
    page = page + "</ul> <p>Mes groupes genres des Bands sont :<p><ul>"
    for b in bands:
        page = page + "<li>" + b.genre + "</li>"
    page = page + "</ul>"
        
    return HttpResponse(page)    

def hello(request):
    response = requests.get("http://127.0.0.1:8000/bands/")
    # bandits = Band.objects.all()
    data = response.json()
    return render(request, 'listeur/info.html', {'data': data})
