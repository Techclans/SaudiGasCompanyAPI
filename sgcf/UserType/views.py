from django.shortcuts import render
#from . import models
from UserType.models import UserType
from UserType.serializers import clsUserType
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer
from django.contrib.auth.decorators import permission_required
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets


class vwUserType(viewsets.ModelViewSet):       
    queryset = UserType.objects.all()
    serializer_class = clsUserType

    #vrSerialier = clsNdmoSector(serializers_class, many=True)
    #return Response({'NdmoSector': serializers_class.data})
    #authentication_classes = [SessionAuthentication]
    #permission_classes = [IsAuthenticated, DjangoModelPermissions]
