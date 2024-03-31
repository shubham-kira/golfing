from django.contrib import admin
from .models import tournament, play, player

admin.site.register(tournament)
admin.site.register(play)
admin.site.register(player)