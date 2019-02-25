from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class SchoolsConnBaseUser(AbstractUser):
    '''
    Model for a custom user
    '''
    phone = models.CharField(max_length=20)  