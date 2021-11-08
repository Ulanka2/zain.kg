from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class UserType(models.TextChoices):
        ADMIN = 'admin'
        STAFF = 'staff'
        BASE_USER = 'base_user'
    user_type = models.CharField(max_length=50, choices=UserType.choices, default=UserType.BASE_USER)