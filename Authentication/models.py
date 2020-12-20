from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class AccountManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, phone_number, password):

        if not email:
            return ValueError('Email field is empty')
        if not first_name:
            return ValueError('first_name field is empty')
        if not last_name:
            return ValueError('last_name field is empty')
        if not phone_number:
            return ValueError('phone_number field is empty')
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone_number, password):

        user = self.create_user(            
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
            password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)

        return user



class Account(AbstractBaseUser):

    email               = models.EmailField(verbose_name='email', max_length=70, unique=True)
    first_name          = models.CharField(max_length=30)
    last_name           = models.CharField(max_length=30)
    phone_number        = models.IntegerField()
    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_superuser        = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    objects =AccountManager()

    def __str__(self):
        return self.email 

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
