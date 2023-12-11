from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (BetViewSet, EventViewSet, HorseViewSet, OddsViewSet,
                    RaceViewSet)

router = DefaultRouter()
router.register(r'races', RaceViewSet)
router.register(r'events', EventViewSet)
router.register(r'horses', HorseViewSet)
router.register(r'bets', BetViewSet)
router.register(r'odds', OddsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
