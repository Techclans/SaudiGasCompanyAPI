
from django.contrib import admin
from django.urls import path,include
from .views import vwUserType
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('apiUserType', vwUserType)



urlpatterns = [

    path('', include(router.urls))

]
