from django.contrib import admin
from django.urls import path, include
from .views import vsCustomer

from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('apiCustomer', vsCustomer, basename='Customer')

urlpatterns = [
    path('', include(router.urls)),
]
