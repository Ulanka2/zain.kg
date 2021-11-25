from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


class User(AbstractUser):
    class UserType(models.TextChoices):
        ADMIN = 'admin'
        STAFF = 'staff'
        BASE_USER = 'base_user'
    user_type = models.CharField(max_length=50, choices=UserType.choices, default=UserType.BASE_USER)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "http://127.0.0.1:8000{}confirm/ ?token={}".format(reverse('password_reset:reset-password-request'), 
    reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "azimovu55@gmail.com",
        # to:
        [reset_password_token.user.email]
    )