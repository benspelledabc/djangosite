# Generated by Django 3.0.7 on 2020-11-08 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deer_harvest_logbook', '0002_auto_20200901_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='harvests',
            name='dnr_confirmation',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]