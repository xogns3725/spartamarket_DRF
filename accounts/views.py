from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from .models import User
from .serializers import UserPasswordSerializer, UserSerializer

class UserListAPIView(APIView):
    def get_object(self, username):
        return get_object_or_404(User, username=username)
    
    def get(self, request, username):
        user = self.get_object(username)
        if request.user.username == user.username:
                serializer = UserSerializer(user)
                return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def put(self, request, username):
        user = self.get_object(username)
        if request.user.username == user.username:
            serializer = UserSerializer(
                user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            
    def delete(self, request):
        user = get_object_or_404(User, username=request.user.username)
        password = request.data.get('password')
        if check_password(password, user.password):
            user.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class UserUpdateAPIView(APIView):
    def put(self, request):
        user = get_object_or_404(User, username=request.user.username)
        serializer = UserPasswordSerializer(
            user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)