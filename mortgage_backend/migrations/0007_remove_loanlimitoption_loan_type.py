# Generated by Django 4.1.7 on 2023-03-24 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mortgage_backend', '0006_loanlimitoption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loanlimitoption',
            name='loan_type',
        ),
    ]
