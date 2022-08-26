from itertools import product
from django.db import models
from product.models import Product
from user.serializers import User
from django.db import models
from django.conf import settings
from rest_framework.authtoken.models import Token
from cart.models import Cart
from django.dispatch import receiver
from django.db.models.signals import post_save

class Order(models.Model):
    address=models.CharField(max_length=100,null=True)
    product= models.ForeignKey(Product, on_delete=models.CASCADE,related_name="orderProduct",null=True)
    customer= models.ForeignKey(User, on_delete=models.CASCADE,related_name="Customer",null=True)
    count=  models.IntegerField(null=True,default=1)
    price= models.IntegerField(null=True)
    orderstatus=models.CharField(max_length=100,null=True)
    
    





    
