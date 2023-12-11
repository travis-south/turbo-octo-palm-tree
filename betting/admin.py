from django.contrib import admin
from .models import Race, Horse, Bet, Odds, Event

admin.site.register(Race)
admin.site.register(Horse)
admin.site.register(Bet)
admin.site.register(Odds)
admin.site.register(Event)
