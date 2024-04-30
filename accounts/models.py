from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # username, Email, 가입일, 비번, 닉네임, 생일, 성별, 자기소개, 이름
    # 이름, 닉네임, 성별, 자기소개
    # 성별, 자기소개 생략가능
    # username, email 중복 x
    email = models.EmailField(unique=True, null=False)
    name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=20)
    birthday = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    introduction = models.TextField(null=True)