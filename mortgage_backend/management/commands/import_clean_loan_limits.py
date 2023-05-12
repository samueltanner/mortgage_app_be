from django.core.management.base import BaseCommand
from mortgage_backend.models import LoanLimitOption
import csv


class Command(BaseCommand):
    help = 'Loads data from a CSV file into the LoanLimitOption model'

    def add_arguments(self, parser):
        parser.add_argument('csvfile', type=str)
        parser.add_argument('effective_date', type=str)

    def handle(self, *args, **options):
        with open(options['csvfile'], newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            for row in reader:
                limit = LoanLimitOption(one_unit=row[0], two_unit=row[1],
                                        three_unit=row[2], four_unit=row[3], effective_date=options['effective_date'])
                limit.save()

        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
