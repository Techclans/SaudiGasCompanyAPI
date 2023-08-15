from django.contrib import admin
from django.urls import path, include
from .views import vsCity

from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('apiCity', vsCity, basename='City')

urlpatterns = [
    path('', include(router.urls)),
]
