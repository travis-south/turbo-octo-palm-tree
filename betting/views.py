
from rest_framework import viewsets

from .models import Bet, Event, Horse, Odds, Race
from .serializers import (BetSerializer, EventSerializer, HorseSerializer,
                          OddsSerializer, RaceSerializer)


class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class HorseViewSet(viewsets.ModelViewSet):
    queryset = Horse.objects.all()
    serializer_class = HorseSerializer

class BetViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer

class OddsViewSet(viewsets.ModelViewSet):
    queryset = Odds.objects.all()
    serializer_class = OddsSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
