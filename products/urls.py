from django.urls import path
from products.views import ProductListAPIView

urlpatterns = [
    path("", ProductListAPIView.as_view(), name="product_list"),
    path("<int:productID>/", ProductListAPIView.as_view(), name="product_modify"),
]