from django.db import models

from django.contrib import admin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import ASCIIUsernameValidator


class User(AbstractBaseUser):
    username = models.CharField(
        max_length=64, unique=True,)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, unique=True)
    is_staff = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_developer = models.BooleanField(default=False)
