from levelupapi.models.gamer import Gamer
from levelupapi.models.events import Event
from django.db import models

class EventGamers(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
