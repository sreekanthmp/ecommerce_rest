from django.db import models


from product.models import Product

from user.serializers import User

    
class Cart(models.Model):

    product= models.ForeignKey(Product, on_delete=models.CASCADE,related_name="CartProduct",null=True)
    count= models.IntegerField()
    customer= models.ForeignKey(User, on_delete=models.CASCADE,related_name="Customer1",null=True)
    price= models.IntegerField()
    
    
    

    

