from rest_framework import serializers
from Lookups.models import Lookup

class clsLookup(serializers.ModelSerializer):
    class Meta:
        model = Lookup
        fields = ('sysid','nameen','namear')
