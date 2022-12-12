
from rest_framework import viewsets
from django.http.response import JsonResponse
from rest_framework import status
 
from ArduinoServer.models import *
from ArduinoServer.serializers import *

class DonneeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Donnee.objects.all()
    serializer_class = DonneeSerializer
    #permission_classes = [permissions.IsAuthenticated]
class DonneesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Donnees.objects.all()
    serializer_class = DonneesSerializer
    #permission_classes = [permissions.IsAuthenticated]


def arduino_list(request):
    if request.method == 'GET':
        ArduinoServer = Donnee.objects.all()
        
        ArduinoServer_serializer = DonneeSerializer(ArduinoServer, many=True)
        return JsonResponse(ArduinoServer_serializer.data[len(ArduinoServer_serializer.data) - 1], safe=False)
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
         'nom_capteur' : val3
        }
        #Temp =  Donnee.objects.all()
        #Temp[1].title = val1
        #Temp[1].Value = val2
        #Temp[1].Valnom_capteurue = val3
        #print(Temp)
        temp_serializer = DonneeSerializer(data=temp)
        
        if temp_serializer.is_valid():
            #Temp.save()
            temp_serializer.save()
            return JsonResponse(temp_serializer.data, status=status.HTTP_201_CREATED) 
        
        return JsonResponse(temp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def arduino_list2(request):
    if request.method == 'GET':
        ArduinoServer = Donnees.objects.all()
        
        ArduinoServer_serializer = DonneesSerializer(ArduinoServer, many=True)
        return JsonResponse(ArduinoServer_serializer.data[len(ArduinoServer_serializer.data) - 1], safe=False)
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
         'nom_capteur' : val3
        }
        #Temp =  Donnee.objects.all()
        #Temp[1].title = val1
        #Temp[1].Value = val2
        #Temp[1].Valnom_capteurue = val3
        #print(Temp)
        temp_serializer = DonneesSerializer(data=temp)
        
        if temp_serializer.is_valid():
            #Temp.save()
            temp_serializer.save()
            return JsonResponse(temp_serializer.data, status=status.HTTP_201_CREATED) 
        
        return JsonResponse(temp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
