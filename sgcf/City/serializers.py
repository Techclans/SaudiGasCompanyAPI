from rest_framework import serializers
from .models import mdlCity

class srlCity(serializers.ModelSerializer):
    class Meta:
        model = mdlCity
        fields = ('sysid','nameen','namear')
