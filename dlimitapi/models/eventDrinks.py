from django.db import models

class EventDrink(models.Model):

    drink_id = models.ForeignKey("Drink", on_delete=models.CASCADE)
    event_id = models.ForeignKey("Event", on_delete=models.CASCADE)
    time_drank = models.TimeField(auto_now=False, auto_now_add=False)