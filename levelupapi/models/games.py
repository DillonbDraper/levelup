from levelupapi.models.game_types import GameType
from levelupapi.models.gamer import Gamer
from django.db import models
from django.db.models.fields.related import ForeignKey


class Game(models.Model):

    title = models.CharField(max_length=100)
    maker = models.CharField(max_length=100, default="Bill")
    gamer = ForeignKey(Gamer, on_delete=models.CASCADE)
    gametype = ForeignKey(GameType, on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    skill_level =  models.CharField(max_length=255)

