# run this script in a shell with python manage.py shell and copy the code into the terminal

import csv
from mortgage_backend.models import County
from mortgage_backend.models import LoanLimit

with open('mortgage_backend/loan_limits.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        state_abbr = row[1]
        county_name = row[4]
        loan_limit = LoanLimit(
            county=County.objects.get(
                state_abbr=state_abbr, county_name=county_name),
            conventional_one_unit=row[7],
            conventional_two_unit=row[8],
            conventional_three_unit=row[9],
            conventional_four_unit=row[10],
            fha_one_unit=row[13],
            fha_two_unit=row[14],
            fha_three_unit=row[15],
            fha_four_unit=row[16],
            conventional_effective_date='2023-01-01',
            fha_effective_date='2023-01-01'
        )
        loan_limit.save()
