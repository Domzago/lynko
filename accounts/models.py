from django.db import models

from django.contrib.auth.models import AbstractUser

class Plan(models.Model):
    name = models.CharField(max_length=255)
    max_num_links = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class User(AbstractUser):
    plan = models.ForeignKey(Plan, related_name='users', default=1, on_delete=models.CASCADE)
