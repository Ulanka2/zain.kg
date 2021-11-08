from rest_framework.views  import  APIView
from accounts.serializers import RegistrationSerializer, LoginSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import  IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes

from rest_framework import generics, status
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

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
        username =serializer.validated_data.get('username')
        password =serializer.validated_data.get('password')
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



# class RequestPasswordResetEmail(generics.GenericAPIView):
#     serializer_class = ResetPasswordEmailRequestSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)

#         email = request.data.get('email', '')

#         if User.objects.filter(email=email).exists():
#             user = User.objects.get(email=email)
#             uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
#             token = PasswordResetTokenGenerator().make_token(user)
#             current_site = get_current_site(
#                 request=request).domain
#             relativeLink = reverse(
#                 'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

#             redirect_url = request.data.get('redirect_url', '')
#             absurl = 'http://'+current_site + relativeLink
#             email_body = 'Hello, \n Use link below to reset your password  \n' + \
#                 absurl+"?redirect_url="+redirect_url
#             data = {'email_body': email_body, 'to_email': user.email,
#                     'email_subject': 'Reset your passsword'}
#             Util.send_email(data)
#         return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)