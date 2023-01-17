from rest_framework import serializers 
from Entreprise.models import *
 
 
class PersonnelSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Personnel
        fields = ('Nom', 'Prenom',  'Age',  'Departement', 'Entreprise', 'sexe')
        
class EntrepriseSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Entreprise
        fields = ('Nom', 'Location',  'ServiceOffert', 'Departement', 'Type')