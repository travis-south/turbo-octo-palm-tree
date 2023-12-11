from celery import shared_task


@shared_task
def recalculate_odds(param):
    # Task implementation
    print(f"Executing task with param: {param}")
    # Run recalculate odds logic here
    pass

@shared_task
def distribute_winnings_task(race_id):
    from .models import distribute_winnings
    distribute_winnings(race_id)
