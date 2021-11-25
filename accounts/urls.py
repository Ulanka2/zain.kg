from django.urls import path
from accounts.views import RegistrationAPIView, LoginAPIView, LogoutAPIView, GetUserAPIView
from .views import ChangePasswordView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('user/', GetUserAPIView.as_view()),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

]



# {
#   "username": "Ulanka00",
#   "email": "user0001@example.com",
#   "password": "qwertyuiopsds",
#   "first_name": "ulan11",
#   "last_name": "Azimov11",
# }

