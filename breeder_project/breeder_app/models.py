from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from .managers import BreederManager


class Breeder(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator()]
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = BreederManager()


class Cat(models.Model):
    breed = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=50, null=False)
    weight = models.IntegerField(null=False)
    height = models.FloatField(null=False)
    lifetime_from = models.IntegerField(null=False)
    lifetime_to = models.IntegerField(null=False)
    name = models.CharField(max_length=150, null=False)
    age = models.IntegerField(null=False)
    photo_link = models.URLField(null=True)
    breeder = models.ForeignKey(
        to=Breeder,
        to_field="id",
        on_delete=models.CASCADE
    )
