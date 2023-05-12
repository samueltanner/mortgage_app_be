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


