from rest_framework import serializers
from UserType.models import UserType

class clsUserType(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields =('sysid','nameen','namear')