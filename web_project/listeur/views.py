from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    return HttpResponse(
        '<h1>HelloWord Django</h1>'
    )

def test(request):
    return HttpResponse(
        "<!DOCTYPE html><html><head><title>Tableau HTML</title><style>p, ul, li, h1{font-display: center ;background-color: cadetblue;border-radius: 20px;}</style></head><body class='BodyDesign'><p class='Paragraph'><h1><u>Un premier paragraphe.</u></h1><br> <!-- Et voici des commentaires en HTML--><br> <!-- Cette balise permet de faier un saut de ligne.--><i>Ici ce trouve un texte en italique.</i><b>Et par la suite un texte en gras.</b></p><ul>Et voici une liste non ordonnee en HTML.<li>Premier element.</li><li>Deuxieme element.</li></ul><br></body></html>"
    )
