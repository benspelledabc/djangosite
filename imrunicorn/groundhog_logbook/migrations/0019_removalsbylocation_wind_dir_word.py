# Generated by Django 3.0.7 on 2021-03-12 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groundhog_logbook', '0018_auto_20210312_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='removalsbylocation',
            name='wind_dir_word',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
