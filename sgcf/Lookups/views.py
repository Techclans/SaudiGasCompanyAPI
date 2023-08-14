from django.shortcuts import render
#from . import models
from Lookups.models import Lookup
from .serializers import clsLookup
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer

#

# Create your views here.
@api_view(['GET','POST'])
def vwLookup(request):

    if request.method == 'GET':
        vrLookup = Lookup.objects.all()
        vrSerialier = clsLookup(vrLookup, many=True)
        return Response({'Lookup':vrSerialier.data})


    elif request.method == 'POST':
        vrSerialier = clsLookup(data=request.data)
        if vrSerialier.is_valid():
            vrSerialier.save()
            return Response({'Lookup':vrSerialier.data}, status=status.HTTP_201_CREATED)
        return Response({'Lookup':vrSerialier}.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def vwLookupID(request,pk):
    try:
        vrLookup = Lookup.objects.get(pk=pk)
    except Lookup.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        vrSerialier = clsLookup(vrLookup)
        return Response({'Lookup':vrSerialier.data})

    elif request.method == 'PUT':
        vrSerialier = clsLookup(vrLookup,data=request.data)
        if vrSerialier.is_valid():
            vrSerialier.save()
            return Response({'Lookup':vrSerialier.data})
        return Response({'Lookup':vrSerialier}.error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vrLookup.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
