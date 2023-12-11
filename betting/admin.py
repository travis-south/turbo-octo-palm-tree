from django.contrib import admin

from .models import Bet, Event, Horse, Odds, Race

admin.site.register(Race)
admin.site.register(Horse)
admin.site.register(Bet)
admin.site.register(Odds)
admin.site.register(Event)
