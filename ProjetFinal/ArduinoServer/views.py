from django.shortcuts import render

from rest_framework import permissions
from rest_framework import viewsets
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from ArduinoServer.models import *
from ArduinoServer.serializers import DonneeSerializer
from rest_framework.decorators import api_view

class DonneeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Donnee.objects.all()
    serializer_class = DonneeSerializer
    #permission_classes = [permissions.IsAuthenticated]

@api_view(['GET', 'POST', 'DELETE'])
def arduino_list(request):
    if request.method == 'GET':
        ArduinoServer = Donnee.objects.all()
        
        ArduinoServer_serializer = DonneeSerializer(ArduinoServer, many=True)
        return JsonResponse(ArduinoServer_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        print("Post request")
        #DonneesData = JSONParser().parse(request)
        #print(DonneesData)
        val1= request.POST["nom"]
        val2 = request.POST["val"]
        val3 = request.POST["id_micro"]
        print("Nom " + val1 + " Value : " + val2)
        
        temp = {
         'title': val1,
         'Valeur': val2,
         'id_uc' : val3
        }
        #Temp =  Donnee()
        #Temp.name = Nom
        #Temp.Value = Value
        #Temp.save()
        #print(Temp)
        temp_serializer = DonneeSerializer(data=temp)
        
        if temp_serializer.is_valid():
            temp_serializer.save()
            return JsonResponse(temp_serializer.data, status=status.HTTP_201_CREATED) 
        
        return JsonResponse(temp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
