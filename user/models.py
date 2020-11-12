from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    phone = models.IntegerField(blank=True, null=True)
    bank = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user'
