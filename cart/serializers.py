
from cart.models import Cart
from rest_framework import serializers


class CartSerializers(serializers.ModelSerializer):
    product=serializers.CharField(source='product.product_name')
    customer=serializers.CharField(source='customer.username')
  
    class Meta:
        model=Cart
        fields=["product","count","customer","price"]
        
        

class Cart1Serializers(serializers.ModelSerializer):   

    class Meta:
        model=Cart
        fields=["product","count","customer","price"]
        
        
