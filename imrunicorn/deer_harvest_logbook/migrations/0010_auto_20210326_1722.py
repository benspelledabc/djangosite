# Generated by Django 3.0.7 on 2021-03-26 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deer_harvest_logbook', '0009_auto_20210326_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='harvests',
            name='location',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]