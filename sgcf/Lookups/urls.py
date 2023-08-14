from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
#    path('admin/', admin.site.urls),
    path('apiLookup/', views.vwLookup),
    path('apiLookup/<int:pk>',views.vwLookupID)
]
