# Generated by Django 3.0.7 on 2021-02-01 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groundhog_logbook', '0009_auto_20210106_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='removalsbylocation',
            name='cloud_level',
            field=models.CharField(choices=[('Clear Sky', 'Clear Sky'), ('Few Clouds', 'Few Clouds'), ('Scattered Clouds', 'Scattered Clouds'), ('Broken Clouds', 'Broken Clouds'), ('Shower/Rain', 'Shower/Rain'), ('Rain', 'Rain'), ('Thunderstorm', 'Thunderstorm'), ('Snow', 'Snow'), ('Mist', 'Mist'), ('Unknown', 'Unknown')], default='Unknown', max_length=20),
        ),
    ]
