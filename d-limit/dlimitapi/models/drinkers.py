from django.db import models
from django.contrib.auth.models import User


class Drinker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.IntegerField(max_length=55)
    age = models.IntegerField(max_length=55)
    weight = models.IntegerField(max_length=55)