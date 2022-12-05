from rest_framework import serializers 
from ArduinoServer.models import *
 
 
class DonneeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Donnee
        fields = ('title', 'Valeur',  'register_date')