from django.db import models

class Event(models.Model):
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    drinker = models.ForeignKey("Drinker", on_delete=models.CASCADE)
    