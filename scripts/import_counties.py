#run this script in a shell with python manage.py shell and copy the code into the terminal
from mortgage_backend.models import County
import csv


with open('mortgage_backend/loan_limits.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        county = County(county_name=row[4], state=row[2],
                        state_abbr=row[1], median_home_value=row[5])
        county.save()
