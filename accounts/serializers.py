from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name',
                    'nickname', 'birthday', 'gender', 'introduction']
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'password': {'required': True},
            'name': {'required': True},
            'nickname': {'required': True},
            'birthday': {'required': True}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields.pop('password')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user

    def validate_password(self, value):
        validate_password(value)
        return value

class UserPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['password']

    def validate(self, data):
        new_password = data.get('password')
        validate_password(new_password)
        user = self.instance
        if user and check_password(new_password, user.password):
            raise ValidationError("비밀번호가 이전과 같습니다.")
        return data
    
    def update(self, instance, validated_data):
        instance.password = make_password(validated_data['password'])
        instance.save()
        return instance

