from django.db import models
from django.contrib.auth.models import User


class Drinker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField()
    age = models.IntegerField()
    weight = models.IntegerField()