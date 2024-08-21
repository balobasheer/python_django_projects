from django.db import models
from django.contrib.auth.models import User
from PIL import Image


from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200,  null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avater = models.ImageField(null=True, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
