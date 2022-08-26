"""ecomm URL Configuration

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
from django.contrib import admin
from django.urls import path

from user import views as user_views
from order import views  as order_views
from product import views  as product_views
from cart import views  as cart_views

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',user_views.register.as_view(),name='register'),
    path("login",obtain_auth_token,name="login"),
    path('logout',user_views. Logout.as_view(),name='logout'),

    path('myuser',user_views.getuserdetails.as_view(),name="myuser"),
    path('product',product_views.Productlist.as_view(),name='product'),
    path('myorder',order_views.Myorder.as_view(),name='order'),
    path('mycart',cart_views.Mycart.as_view(),name='mycart'),        
    path('cartorder',order_views.CartOrder.as_view(),name='cartorder'),
    








]
