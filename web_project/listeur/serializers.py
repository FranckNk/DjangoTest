from django.contrib.auth.models import User, Group
from listeur.models import *
from rest_framework import serializers



class BandsViews(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['name', 'genre', 'biography', 'year_formed', 'official_homepage']


class ListeurViews(serializers.ModelSerializer):
    class Meta:
        model = Listeur
        fields = ['title', 'description', 'year']