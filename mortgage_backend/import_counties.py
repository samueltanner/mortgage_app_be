from mortgage_backend.models import County
import csv


with open('mortgage_backend/loan_limits.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        county = County(name=row[4], state=row[2],
                        state_abbr=row[1], median_home_value=row[5])
        county.save()
