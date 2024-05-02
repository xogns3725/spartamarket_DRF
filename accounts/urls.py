from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.views import LogoutView, UserListAPIView, UserUpdateAPIView

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_list"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password/", UserUpdateAPIView.as_view(), name="profile_detail"),
    path("<str:username>/", UserListAPIView.as_view(), name="profile_detail"),
    
]