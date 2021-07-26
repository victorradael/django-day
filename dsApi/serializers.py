from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Athlete

class AthletsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Athlete
        fields = ['id', 'name', 'height', 'weight', 'age']