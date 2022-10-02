from datetime import datetime
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
    