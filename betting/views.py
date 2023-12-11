
from rest_framework import viewsets
from .models import Race, Horse, Bet, Odds, Event
from .serializers import RaceSerializer, HorseSerializer, BetSerializer, OddsSerializer, EventSerializer

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
