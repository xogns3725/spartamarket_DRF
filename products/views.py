from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProductListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_object(self, productID):
        return get_object_or_404(Product, id=productID)
    
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 3
        
        products = Product.objects.all()
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(result_page, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        author = request.user
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=author)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
    def put(self, request, productID):
        product = self.get_object(productID)
        if product.author == request.user:
            serializer = ProductSerializer(
                product, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, productID):
        product = self.get_object(productID)
        if product.author == request.user:
            product.delete()
            data = {"pk": f"{productID} is deleted."}
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)