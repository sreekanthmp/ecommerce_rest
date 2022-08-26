from itertools import product
from urllib import request
from django.shortcuts import render
from cart.serializers import Cart1Serializers, CartSerializers
from product.models import Product

from . models import Cart


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.permissions import DjangoModelPermissions
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

   
        
class Mycart(APIView):
    permission_classes=(IsAuthenticated,)
    
    def get(self,request):
        user = (request.user)
        
        Data= Cart.objects.filter(customer=user)

        serializer=CartSerializers(Data,many=True) 
        return Response(serializer.data)
        
    
    def post(self,request):
        data_payload = request.data
        data_payload['customer'] = request.user.id
        product = request.data.get("product")
        product1=Product.objects.filter(id=product)
        ids = product1.values_list('price', flat=True)
        count = request.data.get("count")
        for i in range(len(ids)):
            price=ids[i]
            total_price=price*count
            data_payload['price'] = total_price
            serializer = Cart1Serializers(data=data_payload)
            
            if serializer.is_valid():          
                serializer.save()
            else:
                return Response(serializer.errors,status=status.HTTP_201_CREATED)
      
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request,pk=None):
        cartid = request.query_params["id"]
        cart = get_object_or_404(Cart,customer=request.user.id,id=cartid)
        cart.delete()
        return Response({"status":'deleted'},status=status.HTTP_201_CREATED)
    
    
    
    def put(self, request,pk=None):
        cartId = request.query_params["id"]
        
        cart = get_object_or_404(Cart,customer=request.user.id,id=cartId)
        data=request.data
        
        cart.count = data["count"]
        count = request.data.get("count")
        products=Product.objects.filter(id=product)

        ids = products.values_list('price', flat=True)
        price=count*ids

        cart.price=data["price"]
        cart.save()
        return Response({"status":'order status updated'},status=status.HTTP_201_CREATED)
    
                       
        
                      
                
       
    