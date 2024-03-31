from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    age = models.IntegerField(default=0)
    handicap = models.IntegerField(default=0)
    registration_date = models.DateField(auto_now_add = True)
    no_of_tournaments = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user.username)

    def get_player_id(self):
        return self.id


class tournament(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField()
    no_of_players = models.BigIntegerField(default=0)
    start_date = models.DateField()
    winner_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_tournament_id(self):
        return self.id

class play(models.Model):
    player = models.ForeignKey('player', on_delete=models.PROTECT)
    tournament = models.ForeignKey('tournament', on_delete=models.PROTECT)
    no_of_strokes = models.IntegerField()
    score = models.IntegerField()

    class Meta:
        unique_together = ('player', 'tournament')

    def __str__(self):
        return str(self.player.user.username) + "|" + str(self.tournament.name)
