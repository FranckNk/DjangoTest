from rest_framework import serializers 
from Entreprise.models import *
 
 
class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        #fields = "__all__"
        fields = ('Nom', 'Prenom',  'Age',  'Departement', 'sexe', 'Salaire', 'Poste', 'Entreprise', 'Entreprise_name', 'Entreprise_type', 'Entreprise_dep')
    
    Entreprise_name = serializers.CharField(source='Entreprise.Nom')
    Entreprise_type = serializers.CharField(source='Entreprise.Type')
    Entreprise_dep = serializers.CharField(source='Entreprise.Departement')
        
class EntrepriseSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Entreprise
        fields = ('id', 'Nom', 'Location',  'ServiceOffert', 'Departement', 'Type')