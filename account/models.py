from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField(
        max_length=40, unique=True
        )
    name = models.CharField(
        max_length=30, verbose_name='نام'
        )
    last_name = models.CharField(
        max_length=60, verbose_name='نام خانوادگی'
        )
    father_name = models.CharField(
        max_length=30, verbose_name='نام پدر', null=False, blank=False
        )
    national_code = models.CharField(
        max_length=10, verbose_name='کد ملی', null=False, blank='False'
        )
    hamgam_or_pressonel_code = models.CharField(
        max_length=25, verbose_name='کد همگام/پرسنلی'
        )
    avatar = models.ImageField(
        null=False, blank=False, upload_to='account/avatar/', default='defualts/user.png'
    )
    is_student = models.BooleanField(
        verbose_name='دانش آموز', default=True
    )
    is_teacher = models.BooleanField(
        verbose_name='معلم', default=False
    )

    USERNAME_FIELD = 'username'

