from pickletools import read_uint1
from django.http import HttpResponse
from django.shortcuts import render
from Ecole.models import eleve
from Ecole.models import enseignant

def info(request):
    etudiants = eleve.objects.all()
    enseignants = enseignant.objects.all()
    return render(request, 'ecole/info.html',
                  {'etudiants': etudiants})
