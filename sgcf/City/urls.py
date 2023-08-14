from django.contrib import admin
from django.urls import path, include
from .views import CityView

from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('apiCity', CityView, basename='City')

urlpatterns = [
    path('', include(router.urls)),
]
