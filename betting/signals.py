from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from .tasks import recalculate_odds, distribute_winnings_task
from .models import Race, Bet

@receiver(post_save, sender=Bet)
def trigger_recalculate_odds(sender, instance, created, **kwargs):
    if created:
        print(f"New Bet created: {instance}")
        recalculate_odds.delay(instance.id)

@receiver(post_save, sender=Race)
def race_update_handler(sender, instance, **kwargs):
    if instance.status == 'finished':  # Replace 'finished' with your specific status value
        distribute_winnings_task.delay(instance.id)
