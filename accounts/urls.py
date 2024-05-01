from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import UserListAPIView

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_list"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("logout/", TokenRefreshView.as_view(), name="logout"),
    path("<str:username>/", UserListAPIView.as_view(), name="profile_detail"),
    
]