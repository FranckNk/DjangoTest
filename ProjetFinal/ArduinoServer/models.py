from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Donnee(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    Valeur = models.FloatField()
    register_date = models.DateField(auto_now_add = True)