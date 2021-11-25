from rest_framework import serializers
from rest_framework import exceptions
from django.contrib.auth import password_validation 
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User

User = get_user_model()

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    
    
    def validate_username(self, username):
        if len(username) < 4 or len(username) > 15:
            raise exceptions.ValidationError('Username must be between 4 and 15 characters long')
        return username

    def validate_username(self, username):
        if username.isdigit(): 
            raise exceptions.ValidationError('This username is entirely numeric.')
        return username

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)