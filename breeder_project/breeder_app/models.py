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
