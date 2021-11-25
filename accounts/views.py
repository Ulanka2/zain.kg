from django.core.mail import send_mail
from rest_framework.views  import  APIView
from accounts.serializers import RegistrationSerializer, LoginSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import  IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated 

User = get_user_model()


class RegistrationAPIView(APIView):

    def post(self, request):
        serializer =  RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username =serializer.validated_data.get('username')
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        first_name = serializer.validated_data.get('first_name')
        last_name = serializer.validated_data.get('last_name')
       

        if User.objects.filter(username=username).exists():
            return Response({'message': 'Пользователь с таким именем уже существует'}, 
                             status=status.HTTP_400_BAD_REQUEST)
        
        elif User.objects.filter(email=email).exists():
            return Response({'message': 'Данный email адрес уже зарегистрирован в системе'}, 
                             status=status.HTTP_400_BAD_REQUEST)
    
        user = User.objects.create_user(username=username, email=email, password=password,
                                        first_name=first_name, last_name=last_name)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,}, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key,}, status=status.HTTP_200_OK)
        return Response({'message': 'Не валидные данные'},
                         status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes=[IsAuthenticated, ]

    def post(self, request):
        user = request.user
        token = Token.objects.filter(user=user).first()
        token.delete()
        return Response({'message': 'True'})


class GetUserAPIView(APIView):
    permission_classes=[IsAuthenticated, ]

    def get(self, request):
        user = request.user
        serializers = UserSerializer(user, many=False)
        return Response(serializers.data)
   

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)