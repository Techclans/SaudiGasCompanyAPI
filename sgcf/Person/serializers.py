from rest_framework import serializers
from .models import mdlPerson

class srlPerson(serializers.ModelSerializer):
    class Meta:
        model = mdlPerson
        fields = ('id','fname','lname','mname','age','citycode','mobileno','socialid','emailid')
