from rest_framework import serializers
from .models import mdlSeller

class srlSeller(serializers.ModelSerializer):
    class Meta:
        model = mdlSeller
        fields = ('id','person')
