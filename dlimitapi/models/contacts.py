from django.db import models
from phone_field import PhoneField


class Contact(models.Model):
    name = models.CharField(max_length=254)
    phone = PhoneField(null=False, blank=False, unique=True)
    drinker = models.ForeignKey("Drinker", on_delete=models.CASCADE)
