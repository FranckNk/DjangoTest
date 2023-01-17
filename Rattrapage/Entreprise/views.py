
from rest_framework import viewsets
from django.http.response import JsonResponse
from rest_framework import status
 
from Entreprise.models import *
from Entreprise.serializers import *

class EntrepriseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer
    #permission_classes = [permissions.IsAuthenticated]
class PersonnelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    #permission_classes = [permissions.IsAuthenticated]


def get_entreprise(request):
    if request.method == 'GET':
        EntrepriseData = Entreprise.objects.all()
        Entreprise_serializer = EntrepriseSerializer(EntrepriseData, many=True)
        return JsonResponse(Entreprise_serializer.data, safe=False)
       
    

def get_personnel(request):
    if request.method == 'GET':
        PersonnelData = Personnel.objects.all()
        Personnel_serializer = PersonnelSerializer(PersonnelData, many=True)
        return JsonResponse(Personnel_serializer.data, safe=False)
 

 
