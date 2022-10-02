from django.contrib import admin

# Register your models here.

from listeur.models import Band
from listeur.models import Listeur

class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste
    
admin.site.register(Band, BandAdmin)
admin.site.register(Listeur)

