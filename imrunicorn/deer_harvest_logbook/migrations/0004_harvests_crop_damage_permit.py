# Generated by Django 3.0.3 on 2020-08-31 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deer_harvest_logbook', '0003_auto_20200830_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='harvests',
            name='crop_damage_permit',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]