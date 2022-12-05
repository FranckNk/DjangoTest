from django.contrib.auth.models import User, Group
from listeur.models import *
from rest_framework import serializers



class BandsViews(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['id', 'name', 'genre', 'biography', 'year_formed', 'official_homepage']


class ListeurViews(serializers.ModelSerializer):
    class Meta:
        model = Listeur
        fields = ['id', 'title', 'description', 'year', 'sold', 'type']

class ElevesViews(serializers.ModelSerializer):
    class Meta:
        model = Eleve
        fields = ['id', 'name', 'surname', 'sexe', 'birthday', 'email', 'register_date']
