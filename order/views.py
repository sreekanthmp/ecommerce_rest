from ast import Delete
from functools import partial
from itertools import product
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from order.serializers import   OrderSerializers

from order.serializers import Order1Serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . models import Order
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.permissions import DjangoModelPermissions
from django.contrib.auth.models import User
from cart.models import Cart
from product.models import Product



        
    
class Myorder(APIView):
    permission_classes=(IsAuthenticated,)
    
    
    def get(self,request):
        user = request.user
        Data= Order.objects.filter(customer=user)   
        serializer=OrderSerializers(Data,many=True) 
        return Response(serializer.data)
        

    
    def post(self,request):
        data_payload = request.data
        order=Order.objects.all()
        data_payload['customer'] = request.user.id
        data_payload['orderstatus'] ="ordered"
        product = request.data.get("product")
        product1=Product.objects.filter(id=product)
        ids = product1.values_list('price', flat=True)
        print(ids)
        for i in range(len(ids)):
            data_payload['price'] =ids[i]
            serializer = Order1Serializers(data=data_payload)
            if serializer.is_valid():          
                serializer.save()
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
        return Response(serializer.data,status=status.HTTP_201_CREATED) 
    
    
    
    def delete(self, request,pk=None):
        orderId = request.query_params["id"]
        orders = get_object_or_404(Order,customer=request.user.id,id=orderId)
        orders.orderstatus = "canceled"
        orders.save()
        return Response({"status":'order status updated'},status=status.HTTP_201_CREATED)
        
       
    
    
class CartOrder(APIView):
    permission_classes=(IsAuthenticated,)
            
    def post(self,request):
        data_payload = request.data
        order_total=0
        data_payload['customer'] = request.user.id
        data_payload['orderstatus'] ="ordered"

        cart = Cart.objects.filter(customer=request.user.id)
        ids = cart.values_list('product', flat=True)
        ids_copy = cart.values_list('count', flat=True)
        price_copy=cart.values_list('price', flat=True)
        for i in range(len(ids)):
            data_payload['product'] = ids[i]
            data_payload['count'] = ids_copy[i]
            data_payload['price'] = price_copy[i]
            order_total=order_total+price_copy[i]

            serializer = Order1Serializers(data=data_payload)
            if serializer.is_valid():          
                serializer.save()
                print(data_payload)
            else:
                 return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        return Response({"order_total":order_total},status=status.HTTP_201_CREATED)
    
    
         


    # def post(self, request, format=None):
    #     address = request.data.get("address")
    #     product = request.data.get("product")
    #     customer = request.data.get("customer")
    #     data = {'customer': customer, 'product': product, 'address': address}
    #     serializer = OrderSerializers(data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
