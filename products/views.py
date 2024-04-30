from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework.pagination import PageNumberPagination

class ProductListAPIView(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 3
        
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
        
    def post(self, request):
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            
