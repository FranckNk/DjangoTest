from django.db import models

from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class enseignant(models.Model):
    class Sexe(models.TextChoices):
        Male = 'M'
        Female = 'F'
        Other = 'BI'
    
    name = models.fields.CharField(max_length=100)
    surname = models.fields.CharField(max_length=100)
    birthday = models.fields.IntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2015)], default=2000)
    #genre = models.fields.CharField(max_length=50)
    sex = models.fields.CharField(choices=Sexe.choices, max_length=5, default='M')

class eleve(models.Model):
    class Sexe(models.TextChoices):
        Male = 'M'
        Female = 'F'
        Other = 'BI'
    
    name = models.fields.CharField(max_length=100)
    surname = models.fields.CharField(max_length=100)
    #genre = models.fields.CharField(max_length=50)
    sex = models.fields.CharField(choices=Sexe.choices, max_length=5, default='M')
    birthday = models.fields.IntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2015)], default=2000)
    register_date = models.fields.IntegerField(validators=[MinValueValidator(2018), MaxValueValidator(2022)], default=2020)
    New_student = models.fields.BooleanField(default=True)
    email = models.fields.EmailField(null=True, blank=True)
    enseignant = models.ForeignKey(enseignant, null=True, on_delete=models.SET_NULL)
