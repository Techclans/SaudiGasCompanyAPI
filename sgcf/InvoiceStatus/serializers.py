from rest_framework import serializers
from .models import mdlInvoiceStatus

class srlInvoiceStatus(serializers.ModelSerializer):
    class Meta:
        model = mdlInvoiceStatus
        fields =('sysid','nameen','namear')
