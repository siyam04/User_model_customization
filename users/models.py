from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return str(self.phone_number)



