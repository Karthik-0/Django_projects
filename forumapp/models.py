from django.db import models
from django.contrib.auth.models import AbstractUser


class Thread(models.Model):
    title = models.CharField(max_length=50)


class CustomUser(AbstractUser):
    birth_date = models.DateField(
        blank=True,
        null=True,
        auto_now=False,
        auto_now_add=False)

    def __str__(self):
        return self.username