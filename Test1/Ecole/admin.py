from django.contrib import admin

# Register your models here.
from Ecole.models import eleve
from Ecole.models import enseignant

class EleveAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'surname' , 'sex', 'birthday', 'register_date') # liste les champs que nous voulons sur l'affichage de la liste
class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'surname' , 'sex', 'birthday') # liste les champs que nous voulons sur l'affichage de la liste
    
admin.site.register(eleve, EleveAdmin)
admin.site.register(enseignant, BandAdmin)

