from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Bet, Race
from .tasks import distribute_winnings_task, recalculate_odds


@receiver(post_save, sender=Bet)
def trigger_recalculate_odds(sender, instance, created, **kwargs):
    if created:
        print(f"New Bet created: {instance}")
        recalculate_odds.delay(instance.id)

@receiver(post_save, sender=Race)
def race_update_handler(sender, instance, **kwargs):
    if instance.status == 'finished':
        distribute_winnings_task.delay(instance.id)
