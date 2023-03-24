from mortgage_backend.models import LoanLimitOption
import csv


with open('mortgage_backend/2023-01-01_loan_limits.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        limit = LoanLimitOption(one_unit=row[0], two_unit=row[1],
                                three_unit=row[2], four_unit=row[3], effective_date='2023-01-01')
        limit.save()
