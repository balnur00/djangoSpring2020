from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User, AbstractUser, \
    AbstractBaseUser, PermissionsMixin, UserManager


class MyAbstractUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(max_length=30,
                                unique=True,
                                validators=[username_validator])
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=80, blank=True)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now())

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        abstract = True


class MyUser(MyAbstractUser):
    pass
