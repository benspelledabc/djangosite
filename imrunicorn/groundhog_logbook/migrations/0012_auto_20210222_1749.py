# Generated by Django 3.0.7 on 2021-02-22 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groundhog_logbook', '0011_auto_20210222_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='removalsbylocation',
            name='removal_photos',
            field=models.ManyToManyField(blank=True, null=True, to='groundhog_logbook.RemovalPhoto'),
        ),
    ]
