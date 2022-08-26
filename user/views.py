from .serializers import RegisterSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.filters import SearchFilter
from rest_framework import status
from user import models


# Create your views here.

class register(APIView):
    
    def post(self,request,format=None):
        serializer=RegisterSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
          
            data['response']='registered'
            data['username']=account.username
            data['email']=account.email
            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data)

class getuserdetails(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        Data = User.objects.all()
        serializer=UserSerializer(Data,many=True)
        return Response(serializer.data)
    

class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    
