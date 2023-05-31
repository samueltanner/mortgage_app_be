**Clone the repo**

`git clone https://github.com/samueltanner/mortgage_app_be.git`

**Start a Virtual Environment**

Get a virtual environment running using the virtualenv package. This will create a .env file at the root of the app

`virtualenv mortgage_env`

**Activate the virtual environment**

`source mortgage_env/bin/activate`

**Install Requirements**

Depending on your python version installed globally on your machine (or locally in your virtual env) you will either run:

`pip3 install requirements.text`

or

`pip install requirements.text`

The only difference being pip vs. pip3.

**Create a Secret Key**

Create a file at the root of the project called app_secrets.py

In your console run the following script:

`python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())`

This script will generate a secret key. Copy the out put and paste the result into your app_secrets.py like this:

`SECRET_KEY_STRING = '<SECRET KEY>'`
NOTE: The key needs to be a string, so wrap it in quotes.

**Connecting Settings and Secret Key**
Open up your settings.py folder in the mortgage_app_be sub directory.

Make sure that SECRET_KEY_STRING is being imported form app_secrets NOT from mortgage_app_be.app_secrets.

**Make Migrations**

At the time of writing this, I was an idiot and pushed my db up to github. There's no private data on it so it doesn't matter, but it does make it so none of the commands need to be run. 

`python manage.py makemigration`
`python manage.py migrate`
`python manage.py runserver`

This will get your db started and a server running.

**Create A Super User**
Your old terminal is probably now running a server so create a new window of your console and create a super user by running:

`python manage.py createsuperuser`

This will prompt you to add a username, email, and password.

In your web browser go to localhost:8000/admin and login using your super user credentials. You should now see a screen that shows Groups, Users, Countys (spelled wrong), and Loan limit options!

**Load Counties and Loan Limits Into DB**

Go to this website: https://apps.hud.gov/pub/chums/file_layouts.html#Limits2010

Download the following files:
 1. CY<current year> FHA Forward Limits (FHA Loan Limits)
 2. CY<current year> Fannie/Freddie Limits (Conventional Loan Limits)

Add them to a spreadsheet, remove the first two rows, and save as a .csv file

Run the following command to import both loan limits and associate them to county names:
`python manage.py import_counties_and_limits <PATH TO FHA LIMITS> <PATH TO CONVENTIONAL LIMITS> <DATE OF PUBLICATION eg. 2023-01-01>`