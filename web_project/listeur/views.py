from pickletools import read_uint1
from django.http import HttpResponse
from django.shortcuts import render
from listeur.models import Band

# Create your views here.



def test(request):
    return HttpResponse(
        "<!DOCTYPE html><html><head><title>Tableau HTML</title><style>p, ul, li, h1{font-display: center ;background-color: cadetblue;border-radius: 20px;}</style></head><body class='BodyDesign'><p class='Paragraph'><h1><u>Un premier paragraphe.</u></h1><br> <!-- Et voici des commentaires en HTML--><br> <!-- Cette balise permet de faier un saut de ligne.--><i>Ici ce trouve un texte en italique.</i><b>Et par la suite un texte en gras.</b></p><ul>Et voici une liste non ordonnee en HTML.<li>Premier element.</li><li>Deuxieme element.</li></ul><br></body></html>"
    )

def band(request):
    bands = Band.objects.all()
    page = """\
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>"""
    for a in bands:
        page = page + "<li>" + a.name + "</li>"
    page = page + "</ul>"
    return HttpResponse(page)    

def hello(request):
    bandits = Band.objects.all()
    return render(request, 'listeur/hello.html')
