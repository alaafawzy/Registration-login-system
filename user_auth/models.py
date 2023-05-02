from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
import os
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone_number, email , gender ,  password,  **extra_fields):
        user = self.model(phone_number=phone_number,email=email , gender= gender,  **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email , gender ,  password,  **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(phone_number, email , gender ,  password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    id = models.BigAutoField(primary_key=True)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True , max_length=20)    
    email = models.EmailField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    username = None
    first_name = None
    last_name = None
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email','gender']