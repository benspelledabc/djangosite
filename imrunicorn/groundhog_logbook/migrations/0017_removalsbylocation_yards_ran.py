# Generated by Django 3.0.7 on 2021-03-06 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groundhog_logbook', '0016_removalsbylocation_foot_hold_trapped'),
    ]

    operations = [
        migrations.AddField(
            model_name='removalsbylocation',
            name='yards_ran',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
        ),
    ]
