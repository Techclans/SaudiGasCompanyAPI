"""scgf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.contrib import admin
#from django.dmoconfiget.urls import url
#from dmoconfiget import views
#from .views import getDomain
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

#from BusinessCategory.views import BusinessCategoryViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
#router.register('City', CityView)
#router.register(r'city', CityView, basename='city')
#router.register(r'businesscategory', BusinessCategoryViewSet, basename='BusinessCategory')

urlpatterns = [
   #path('dmo/', views.getDomain.as_view(),)
   path('api/', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('admin/', admin.site.urls),
   path('api-token-auth/',obtain_auth_token,name="api_token_auth"),
   path('',include('City.urls')),
   path('',include('UserType.urls')),
   path('',include('Lookups.urls')),
   path('',include('Customer.urls')),
   path('',include('DelivaryStatus.urls')),
   path('',include('InvoiceStatus.urls')),
   path('',include('Person.urls')),
   path('',include('Seller.urls')),




    
]