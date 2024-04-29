from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
from accounts.views import UserListAPIView

urlpatterns = [
    path("", UserListAPIView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("<str:username>/", UserListAPIView.as_view(), name="profile_detail"),
]