from django.contrib import admin
from django.urls import path, include
from .views import vsSeller

from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('apiSeller', vsSeller, basename='Seller')

urlpatterns = [
    path('', include(router.urls)),
]