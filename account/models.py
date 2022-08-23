from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, national_code, password=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not national_code:
            raise ValueError('Error: The User you want to create must have an username, try again')

        my_user = self.model(
            national_code=self.model.normalize_username(national_code),
        )

        my_user.set_password(password)
        my_user.save(using=self._db)
        return my_user

    def create_staffuser(self, national_code, password):
        """
        Creates and saves a staff user with the given username and password.
        """
        my_user = self.create_user(
            national_code,
            password=password,
        )
        my_user.staff = True
        my_user.save(using=self._db)
        return my_user

    def create_superuser(self, national_code, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        my_user = self.create_user(
            national_code,
            password=password,
        )
        my_user.staff = True
        my_user.admin = True
        my_user.save(using=self._db)
        return my_user

    def get_by_natural_key(self, national_code):
        return self.get(**{self.model.USERNAME_FIELD: national_code})


class User(AbstractBaseUser):
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
        max_length=10, verbose_name='کد ملی', null=False, blank=False, unique=True
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
    is_superuser = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=True, verbose_name='فعال / غیر فعال'
    )

    USERNAME_FIELD = 'national_code'

    objects = UserManager()
