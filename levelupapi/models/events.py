from levelupapi.models.games import Game
from levelupapi.models.gamer import Gamer
from django.db import models
from django.db.models.fields import CharField, DateTimeField
from django.db.models.fields.related import ForeignKey

class Event(models.Model):
    event_time = DateTimeField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    location = CharField(max_length=100)
    scheduler = models.ForeignKey(Gamer, on_delete=models.CASCADE)