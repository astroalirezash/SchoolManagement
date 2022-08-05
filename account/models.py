from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    name = models.CharField
    last_name = models.CharField
    father_name = models.CharField
    national_code = models.CharField
    hamgam_code = models.CharField
    avatar = models.ImageField
    is_student = models.BooleanField
    is_teacher = models.BooleanField

