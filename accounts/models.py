from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    credit = models.BigIntegerField(default=0)
    username = None
    email = models.EmailField(unique=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def update_credit(self,amount):
        if self.credit + amount < 0 and self.is_superuser==False:
            raise Exception("credit cant be negetive ")
        self.credit += amount
        self.save()

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email

    def save(self,*args, **kwargs):
        if self.pk is None:
            self.password = make_password(self.password)
        return super().save(*args, **kwargs)


class CreditProvider(CustomUser):

    business_name = models.CharField(max_length=256)

    class Meta:
        verbose_name = "CreditProvider"


class Customer(CustomUser):

    phone_number = models.CharField(max_length=13)

    class Meta:
        verbose_name = "Customer"
        