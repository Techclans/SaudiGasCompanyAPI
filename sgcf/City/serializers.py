from rest_framework import serializers
from .models import City

class clsCity(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('sysid','nameen','namear')
