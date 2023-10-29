from django.db.models import fields
from rest_framework.utils import model_meta
from .models import Persona
from rest_framework import serializers

class PersonaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'