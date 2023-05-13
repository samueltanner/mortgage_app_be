from django.core.management.base import BaseCommand
from mortgage_backend.models import LoanLimitOption
import csv
from mortgage_backend.models import County, LoanLimitOption

# Go to this website: https://apps.hud.gov/pub/chums/file_layouts.html#Limits2010
# Download the following files:
# CY<current year> FHA Forward Limits & CYCY<current year> Fannie/Freddie Limits
# Add them to a spreadsheet, remove the first two rows, and save as a .csv file
# run this script


class Command(BaseCommand):
    help = "Loads Data from HUD"

    def add_arguments(self, parser):
        parser.add_argument('fha_limits_csv', type=str)
        parser.add_argument('conventional_limits_csv', type=str)
        parser.add_argument('effective_date', type=str)

    def handle(self, *args, **options):
        with open(options['fha_limits_csv'], newline='') as fha_limits_csv:
            reader = csv.reader(fha_limits_csv, delimiter=',')
            next(reader)
            for row in reader:
                data = row[0]
                limit_1_unit = int(data[73:80])
                limit_2_units = int(data[80:87])
                limit_3_units = int(data[87:94])
                limit_4_units = int(data[94:101])
                state_abbr = data[101:103].strip()
                state_name = data[106:132].strip()
                county_name = data[132:147].strip()

                county, created = County.objects.get_or_create(county_name=county_name, state_abbr=state_abbr, state=state_name)

                # Save the county object to ensure it has an ID value assigned
                county.save()

                limit, created = LoanLimitOption.objects.get_or_create(
                    one_unit=limit_1_unit,
                    two_unit=limit_2_units,
                    three_unit=limit_3_units,
                    four_unit=limit_4_units,
                    effective_date=options['effective_date']
                )

                limit.save()

                county.fha_loan_limits.set([limit])

        with open(options['conventional_limits_csv'], newline='') as conventional_limits_csv:
          reader = csv.reader(conventional_limits_csv, delimiter=',')
          next(reader)
          for row in reader:
              data = row[0]
              limit_1_unit = int(data[73:80])
              limit_2_units = int(data[80:87])
              limit_3_units = int(data[87:94])
              limit_4_units = int(data[94:101])
              state_abbr = data[101:103].strip()
              state_name = data[106:132].strip()
              county_name = data[132:147].strip()

              try:
                county = County.objects.get(county_name=county_name, state=state_name, state_abbr=state_abbr)
                if county.county_name == 'PLATTE':
                  print('county', county.county_name, county.state, county.id)
              except County.DoesNotExist:
                print('County does not exist', county_name)

              limit, created = LoanLimitOption.objects.get_or_create(
                    one_unit=limit_1_unit,
                    two_unit=limit_2_units,
                    three_unit=limit_3_units,
                    four_unit=limit_4_units,
                    effective_date=options['effective_date']
                )

              limit.save()

              county.conventional_loan_limits.set([limit])

              county.save()


        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
