# Generated by Django 3.0.7 on 2021-01-07 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groundhog_logbook', '0008_auto_20210105_2032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='removalsbylocation',
            options={'ordering': ('-removal_date', 'shooter', 'shot_distance_yards')},
        ),
    ]
