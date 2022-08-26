from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from product.serializers import  ProductSerializers
from rest_framework.response import Response
from rest_framework import status
from . models import Product


class Productlist(APIView):
    permission_classes=[IsAdminUser]
    def post(self,request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
       

        Data = Product.objects.all()
        serializer=ProductSerializers(Data,many=True)
        return Response(serializer.data)
