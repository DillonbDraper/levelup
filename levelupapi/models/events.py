from levelupapi.models.games import Game
from levelupapi.models.gamer import Gamer
from django.db import models
from django.db.models.fields import CharField, DateField, TimeField
from django.db.models.fields.related import ForeignKey

class Event(models.Model):
    organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    description = CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date = DateField(default= '2021-02-04')
    time = TimeField(default= '12:00')

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
