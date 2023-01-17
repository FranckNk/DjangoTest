from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
    
class Entreprise(models.Model):
    class TypeEntreprise(models.Choices):
        PME = 'PME'
        GE = 'GE'
        Other = 'O'
        
    Nom = models.CharField(max_length=70, blank=False, default='nom')
    Location = models.CharField(max_length=70, blank=False, default='Bathurst')
    ServiceOffert = models.CharField(max_length=70, blank=False, default='Tutorat')
    Departement = models.CharField(max_length=70, blank=False, default='Administration')
    Type = models.CharField(choices=TypeEntreprise.choices, max_length=5, default='M')
    #retourne le nom du model
  
    
class Personnel(models.Model):
    class Sexe(models.TextChoices):
        Male = 'M'
        Female = 'F'
        Other = 'BI'
        
    Nom = models.CharField(max_length=70, blank=False, default='nom')
    Prenom = models.CharField(max_length=70, blank=False, default='prenom')
    Age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    Poste = models.CharField(max_length=70, blank=False, default='prenom')
    Salaire = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    Departement = models.CharField(max_length=20, default='')
    Entreprise = models.ForeignKey(Entreprise, null=True, on_delete=models.SET_NULL)
    sexe = models.CharField(choices=Sexe.choices, max_length=5, default='M')
    #retourne le nom du model
  
