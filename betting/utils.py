import csv
from django.utils.dateparse import parse_datetime
from .models import Race, Horse, Odds, User, distribute_winnings, place_bet
from django.db.models import QuerySet
from django.core.exceptions import ObjectDoesNotExist
from typing import Dict, NoReturn

def handle_race_data(row):
    try:
      # Extracting race information from the row
      race_number = int(row['race_number'])
      race_name = row['race_name']
      race_start_time = parse_datetime(row['race_start_time'])

      # Update or create the race instance
      race, created = Race.objects.update_or_create(
          race_number=race_number,
          defaults={'name': race_name, 'start_time': race_start_time}
      )

      # Assuming horse names are separated by a semicolon in the CSV
      horse_names = row['horses'].split(';')
      for horse_name in horse_names:
          Horse.objects.update_or_create(
              name=horse_name.strip(),  # Strip to remove any leading/trailing whitespaces
              race=race
          )
    except ObjectDoesNotExist:
        pass
    except ValueError:
        # Handle the case where data parsing fails
        pass

def handle_odds(row: Dict[str, str]) -> NoReturn:
    try:
        race_number: int = int(row['race_number'])
        race: QuerySet = Race.objects.get(race_number=race_number)

        horse_name: str = row['horse_name']
        horse: QuerySet = Horse.objects.get(name=horse_name.strip(), race=race)

        odds_value: float = float(row['odds'])

        Odds.objects.update_or_create(
            race=race,
            horse=horse,
            defaults={'odds': odds_value}
        )
    except ObjectDoesNotExist:
        pass
    except ValueError:
        pass

def handle_place_bets(row: Dict[str, str]) -> NoReturn:
    try:
        race_number: int = int(row['race_number'])
        race: QuerySet = Race.objects.get(race_number=race_number)

        horse_name: str = row['horse_name']
        horse: QuerySet = Horse.objects.get(name=horse_name.strip(), race=race)

        user_id: int = int(row['user_id'])
        user: QuerySet = User.objects.get(id=user_id)

        place_bet(race_id=race.id, horse_id=horse.id, user=user, amount=row['amount'])

    except ObjectDoesNotExist:
        pass
    except ValueError:
        pass

def handle_start_race(row: Dict[str, str]) -> NoReturn:
    try:
        race_number: int = int(row['race_number'])
        race: QuerySet = Race.objects.get(race_number=race_number)

        race.status = 'In Progress'
        race.save()

    except Race.DoesNotExist:
        pass
    except ValueError:
        pass

def handle_dividends(row):
    try:
        race_number = int(row['race_number'])
        winning_horse_name = row['winning_horse_name']

        race = Race.objects.get(race_number=race_number)
        winning_horse = Horse.objects.get(name=winning_horse_name, race=race)

        distribute_winnings(race.id, winning_horse.id)

        # Update race status or any other necessary fields post dividend distribution
        race.status = 'Completed'
        race.save()

    except Race.DoesNotExist:
        # Handle the case where the race doesn't exist
        pass
    except Horse.DoesNotExist:
        # Handle the case where the winning horse doesn't exist
        pass
    except ValueError:
        # Handle data parsing errors
        pass

def process_event_csv(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            event_type = row['EVENT_TYPE']

            if event_type == 'RACE_DATA':
                handle_race_data(row)
            elif event_type == 'UPDATE_ODDS':
                handle_odds(row)
            elif event_type == 'PLACE_BETS':
                handle_place_bets(row)
            elif event_type == 'START_RACE':
                handle_start_race(row)
            elif event_type == 'DIVIDENDS':
                handle_dividends(row)
