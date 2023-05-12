from django.core.management.base import BaseCommand
from mortgage_backend.models import County
import csv


class Command(BaseCommand):
    help = 'Loads data from a CSV file into the County model'

    def add_arguments(self, parser):
        parser.add_argument('csvfile', type=str)

    def handle(self, *args, **options):
        with open(options['csvfile'], newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            for row in reader:
                county = County(county_name=row[4], state=row[2],
                                state_abbr=row[1], median_home_value=row[5])
                county.save()

        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))