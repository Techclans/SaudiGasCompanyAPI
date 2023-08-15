from django.contrib import admin
from django.urls import path, include
from .views import vsPerson

from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('apiPerson', vsPerson, basename='Person')

urlpatterns = [
    path('', include(router.urls)),
]