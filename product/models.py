from django.db import models
from django.db import models
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save



class Product(models.Model):

    product_name=models.CharField(max_length=100)
    price=models.IntegerField()


    def __str__(self):
        return self.product_name

    
