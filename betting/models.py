from datetime import datetime
from django.db import models, transaction
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.db.models import Sum
from django.conf import settings
from django.contrib.auth.models import User
from typing import Optional
import json

# Race Model
class Race(models.Model):
    race_number: int = models.IntegerField(unique=True)
    name: str = models.CharField(max_length=200)
    start_time: Optional[datetime] = models.DateTimeField(null=True, blank=True)
    status: str = models.CharField(max_length=20, default='Not Started')

    def __str__(self):
        return self.name

# Horse Model
class Horse(models.Model):
    name: str = models.CharField(max_length=200)
    race: Race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Odds Model
class Odds(models.Model):
    race: Race = models.ForeignKey(Race, on_delete=models.CASCADE)
    horse: Horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    odds: float = models.FloatField()
    timestamp: datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('race', 'horse', 'timestamp')

    def __str__(self):
        return f"{self.race.name} - {self.horse.name} Odds: {self.odds}"

# Bet Model
class Bet(models.Model):
    race: Race = models.ForeignKey(Race, on_delete=models.CASCADE)
    horse: Horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    amount: float = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.amount} on {self.horse.name}"

# Event Model
class Event(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, null=True, blank=True)
    event_type = models.CharField(max_length=100)
    payload = models.JSONField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.event_type} for Race {self.race.race_number if self.race else 'N/A'}"

    def get_payload(self):
        return json.loads(self.payload)


def place_bet(user: User, race_id: int, horse_id: int, amount: float):
    try:
        with transaction.atomic():
            race = Race.objects.get(id=race_id)
            horse = Horse.objects.get(id=horse_id, race=race)

            if not race.is_open_for_betting:
                return "Betting is closed for this race"

            bet = Bet.objects.create(user=user, race=race, horse=horse, amount=amount)

            return "Bet placed successfully"

    except Race.DoesNotExist:
        return "Race does not exist"
    except Horse.DoesNotExist:
        return "Horse does not exist in this race"
    except Exception as e:
        # Log the error
        return str(e)
    
def distribute_winnings(race_id: int, winning_horse_id: int):
    winning_bets = Bet.objects.filter(race_id=race_id, horse_id=winning_horse_id)
    total_bets = Bet.objects.filter(race_id=race_id).aggregate(Sum('amount'))['amount__sum']
    winning_amount = total_bets - (total_bets * (1 - settings.HOUSE_COMMISSION))

    with transaction.atomic():
        for bet in winning_bets:
            # Calculate the share of each winning bet
            share = (bet.amount / total_bets) * winning_amount
            # Update the user's balance
            bet.user.balance += share
            bet.user.save()
