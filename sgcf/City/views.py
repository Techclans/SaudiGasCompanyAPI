from django.shortcuts import render
#from . import models
from .models import City
from .serializers import clsCity
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,viewsets
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
#


class CityView(viewsets.ModelViewSet):    
    queryset = City.objects.all()
    serializer_class = clsCity
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

"""

# Create your views here.
@api_view(['GET','POST'])
def vwCity(request):

    if request.method == 'GET':
        vrCity = City.objects.all()
        vrSerialier = clsCity(vrCity, many=True)
        return Response({'City':vrSerialier.data})


    elif request.method == 'POST':
        vrSerialier = clsCity(data=request.data)
        if vrSerialier.is_valid():
            vrSerialier.save()
            return Response({'City':vrSerialier.data}, status=status.HTTP_201_CREATED)
        return Response({'City':vrSerialier}.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def vwCityID(request,pk):
    try:
        vrCity = City.objects.get(pk=pk)
    except City.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        vrSerialier = clsCity(vrCity)
        return Response({'City':vrSerialier.data})

    elif request.method == 'PUT':
        vrSerialier = clsCity(vrCity,data=request.data)
        if vrSerialier.is_valid():
            vrSerialier.save()
            return Response({'City':vrSerialier.data})
        return Response({'City':vrSerialier}.error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vrCity.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

        
"""
