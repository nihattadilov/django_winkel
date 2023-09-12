from django.db import models
from django.contrib.auth.models import AbstractUser



class BaseUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    picture = models.ImageField(upload_to='users', blank=True)