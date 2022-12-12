from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Donnee(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    Valeur = models.FloatField()
    register_date = models.DateTimeField(auto_now_add = True)
    nom_capteur = models.CharField(max_length=20, default='')
    def __str__(self):
        return self.item
    
class Donnees(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    Valeur = models.FloatField()
    register_date = models.DateTimeField(auto_now_add = True)
    nom_capteur = models.CharField(max_length=20, default='')
    def __str__(self):
        return self.item