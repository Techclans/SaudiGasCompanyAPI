from rest_framework import serializers
from .models import mdlCustomer

class srlCustomer(serializers.ModelSerializer):
    class Meta:
        model = mdlCustomer
        fields = ('sysid','addrline1','addrline2','coordinates','city','person')
