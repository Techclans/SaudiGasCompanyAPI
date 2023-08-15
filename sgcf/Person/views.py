from django.shortcuts import render
#from . import models
from .models import mdlPerson
from .serializers import srlPerson
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,viewsets
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
#


class vsPerson(viewsets.ModelViewSet):    
    queryset = mdlPerson.objects.all()
    serializer_class = srlPerson
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]