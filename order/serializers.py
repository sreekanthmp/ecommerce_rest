
from order.models import Order
from rest_framework import serializers
from product.models import Product
from product.serializers import ProductSerializers



   

class OrderSerializers(serializers.ModelSerializer):
    product=serializers.CharField(source='product.product_name')
    customer=serializers.CharField(source='customer.username')
   
    class Meta:
        model=Order
        fields=["product","customer","address","count","price","orderstatus"]


class Order1Serializers(serializers.ModelSerializer):
    # product = ProductSerializers(many=True, read_only=True)

    class Meta:
        model=Order

        fields=["product","customer","address","price","orderstatus"]
   
   