# Generated by Django 3.0.7 on 2021-01-06 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groundhog_logbook', '0005_auto_20201230_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='removalsbylocation',
            name='cloud_level',
            field=models.CharField(choices=[('Clear Sky', 'Clear Sky'), ('Few Clouds', 'Few Clouds'), ('Scattered Clouds', 'Scattered Clouds'), ('Broken Clouds', 'Broken Clouds'), ('Shower Rain', 'Shower/Rain'), ('Rain', 'Rain'), ('Thunderstorm', 'Thunderstorm'), ('Snow', 'Snow'), ('Mist', 'Mist'), ('Unknown', 'Unknown')], default='Unknown', max_length=20),
        ),
    ]
