from django.db import models
from django.contrib.auth.models import User

class Drink(models.Model):

    type = models.CharField(max_length=55)