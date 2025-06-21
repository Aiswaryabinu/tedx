from django.contrib.auth.models import AbstractUser
from django.db import models

"""This module contains the custom user model for the application, extending Django's AbstractUser."""

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
