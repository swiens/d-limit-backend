from django.db import models

class EventDrink(models.Model):

    drink = models.ForeignKey("Drink", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    time_drank = models.DateTimeField(auto_now=False, auto_now_add=False)