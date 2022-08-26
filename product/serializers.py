# from order.serializers import OrderSerializers
from product.models import Product
from rest_framework import serializers
from user.serializers import User


   

class ProductSerializers(serializers.ModelSerializer):
    # order = OrderSerializers(many=True)

    class Meta:
        model=Product
        fields='__all__'




