from django.contrib import admin
from django.urls import path, include
from .views import vsInvoiceStatus

from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('apiInvoiceStatus', vsInvoiceStatus, basename='InvoiceStatus')

urlpatterns = [
    path('', include(router.urls)),
]
