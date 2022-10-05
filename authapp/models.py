from django.db import models

from django.contrib import admin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.hashers import make_password


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=64, unique=True,)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)

    post = [('admin', 'admin'), ('manager', 'manager'),
            ('developer', 'developer')]
    is_staff = models.CharField(max_length=12, choices=post)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"

    def __str__(self):

        return self.username+' '+self.is_staff
