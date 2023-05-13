from django.core.management.base import BaseCommand
from mortgage_backend.models import LoanLimitOption
import csv
from mortgage_backend.models import County, LoanLimitOption

# Go to this website: https://apps.hud.gov/pub/chums/file_layouts.html#Limits2010
# Download the following files:
# CY<current year> FHA Forward Limits & CYCY<current year> Fannie/Freddie Limits
# Add them to a spreadsheet, remove the first two rows, and save as a .csv file


class Command(BaseCommand):
    help = "Loads Data from HUD"

    def add_arguments(self, parser):
        parser.add_argument('fha_limits_csv', type=str)
        parser.add_argument('conventional_limits_csv', type=str)
        parser.add_argument('effective_date', type=str)

    def handle(self, *args, **options):
        limit_dict = {}
        dict_val = 1

        with open(options['fha_limits_csv'], newline='') as fha_limits_csv:
            reader = csv.reader(fha_limits_csv, delimiter=',')
            next(reader)
            for row in reader:
                data = row[0]
                msa_code = data[0:5].strip()
                met_div_code = data[5:10].strip()
                msa_name = data[10:60].strip()
                soa_code = data[60:65].strip()
                limit_type = data[65:66].strip()
                median_price = int(data[66:73])
                limit_1_unit = int(data[73:80])
                limit_2_units = int(data[80:87])
                limit_3_units = int(data[87:94])
                limit_4_units = int(data[94:101])
                state_abbr = data[101:103].strip()
                county_code = int(data[103:106])
                state_name = data[106:132].strip()
                county_name = data[132:147].strip()
                county_trans_date = int(
                    data[147:155].strip()) if data[147:155].strip() else None
                limit_trans_date = int(data[155:163])
                median_price_limit = int(data[163:170])
                year_for_median_limit = int(data[170:175])

                limit_key = str(limit_1_unit) + ',' + str(limit_2_units) + \
                    ',' + str(limit_3_units) + ',' + str(limit_4_units)

                if (limit_key not in limit_dict):
                    limit_dict[limit_key] = dict_val
                    dict_val += 1

                limit = LoanLimitOption(one_unit=limit_1_unit, two_unit=limit_2_units,
                                        three_unit=limit_3_units, four_unit=limit_4_units, effective_date=options['effective_date'])

                try:
                    LoanLimitOption.objects.get(
                        one_unit=limit_1_unit, two_unit=limit_2_units, three_unit=limit_3_units, four_unit=limit_4_units, effective_date=options['effective_date'])
                except LoanLimitOption.DoesNotExist:
                    limit.save()

                # import counties
                county = County(county_name=county_name, state=state_name,
                                state_abbr=state_abbr, fha_loan_option=limit)

                # county.save()

        with open(options['conventional_limits_csv'], newline='') as conventional_limits_csv:
          reader = csv.reader(conventional_limits_csv, delimiter=',')
          next(reader)
          for row in reader:
              msa_code = int(row[0:5])
              met_div_code = int(row[5:10])
              msa_name = row[10:60].strip()
              soa_code = row[60:65].strip()
              limit_type = row[65:66].strip()
              median_price = int(row[66:73])
              limit_1_unit = int(row[73:80])
              limit_2_units = int(row[80:87])
              limit_3_units = int(row[87:94])
              limit_4_units = int(row[94:101])
              state_abbr = row[101:103].strip()
              county_code = int(row[103:106])
              state_name = row[106:132].strip()
              county_name = row[132:147].strip()
              county_trans_date = int(row[147:155])
              limit_trans_date = int(row[155:163])
              median_price_limit = int(row[163:170])
              year_for_median_limit = int(row[170:175])

              limit_key = str(limit_1_unit) + ',' + str(limit_2_units) + \
                    ',' + str(limit_3_units) + ',' + str(limit_4_units)

              if (limit_key not in limit_dict):
                  limit_dict[limit_key] = dict_val
                  dict_val += 1

              limit = LoanLimitOption(one_unit=limit_1_unit, two_unit=limit_2_units,
                                        three_unit=limit_3_units, four_unit=limit_4_units, effective_date=options['effective_date'])

              try:
                  LoanLimitOption.objects.get(
                      one_unit=limit_1_unit, two_unit=limit_2_units, three_unit=limit_3_units, four_unit=limit_4_units, effective_date=options['effective_date'])
              except LoanLimitOption.DoesNotExist:
                  limit.save()

              county = County.objects.get(county_name=county_name, state=state_name,state_abbr=state_abbr)
              county.conventional_loan_option = limit
              county.save()
        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))



