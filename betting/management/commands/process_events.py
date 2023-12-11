from django.core.management.base import BaseCommand

from ...utils import process_event_csv


class Command(BaseCommand):
    help = 'Processes a CSV file of race event data'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str)

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']
        process_event_csv(csv_file_path)
        self.stdout.write(self.style.SUCCESS('Successfully processed event data'))
