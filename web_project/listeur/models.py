from datetime import datetime
from email.policy import default
import xxlimited
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    
    name = models.fields.CharField(max_length=100)
    #genre = models.fields.CharField(max_length=50)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5, default='HH')
    biography = models.fields.CharField(max_length=1000, default='')
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)], default=2000)
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    
class Listeur(models.Model):
    class Type(models.TextChoices):
        RECORDS = 'R'
        CLOTHING = 'C'
        POSTERS = 'P'
        MISC = 'M'
        
    title =  models.fields.CharField(max_length=100)
    description =  models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=True)
    year = models.fields.IntegerField(validators=[MinValueValidator(1999), MaxValueValidator(2022)], default=2010)
    type = models.fields.CharField(choices=Type.choices, max_length=5, default='M')
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

class Eleve(models.Model):
    class Sexe(models.TextChoices):
        Male = 'M'
        Female = 'F'
        Other = 'BI'
    
    name = models.fields.CharField(max_length=100)
    surname = models.fields.CharField(max_length=100)
    #genre = models.fields.CharField(max_length=50)
    sexe = models.fields.CharField(choices=Sexe.choices, max_length=5, default='M')
    birthday = models.fields.IntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2015)], default=2000)
    register_date = models.fields.IntegerField(validators=[MinValueValidator(2018), MaxValueValidator(2022)], default=2020)
    New_student = models.fields.BooleanField(default=True)
    email = models.fields.EmailField(null=True, blank=True)
