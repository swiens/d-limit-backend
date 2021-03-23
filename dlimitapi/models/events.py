from django.db import models

class Event(models.Model):
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    drinker = models.ForeignKey("Drinker", on_delete=models.CASCADE)
    