# Generated by Django 3.0.7 on 2021-04-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groundhog_logbook', '0021_auto_20210312_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='hole_location_pic',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/groundhog_hole_locations/'),
        ),
    ]
