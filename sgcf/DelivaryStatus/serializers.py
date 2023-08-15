from rest_framework import serializers
from .models import mdlDelivarStatus

class srlDelivarStatus(serializers.ModelSerializer):
    class Meta:
        model = mdlDelivarStatus
        fields =('sysid','nameen','namear')
