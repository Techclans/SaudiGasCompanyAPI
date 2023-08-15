from django.contrib import admin
from django.urls import path, include
from .views import vsDelivarStatus

from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('apiDelivarStatus', vsDelivarStatus, basename='DelivarStatus')

urlpatterns = [
    path('', include(router.urls)),
]
