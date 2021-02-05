from levelupapi.models.game_types import GameType
from levelupapi.models.gamer import Gamer
from django.db import models
from django.db.models.fields.related import ForeignKey


class Game(models.Model):

    title = models.CharField(max_length=100)
    game_type = ForeignKey(GameType, on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    gamer = ForeignKey(Gamer, on_delete=models.CASCADE)
    description =  models.CharField(max_length=255)

