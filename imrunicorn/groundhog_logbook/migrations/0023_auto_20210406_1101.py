# Generated by Django 3.0.7 on 2021-04-06 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groundhog_logbook', '0022_location_hole_location_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='hole_location_pic',
            new_name='hole_location_picture',
        ),
    ]
