# Generated by Django 3.0.7 on 2021-02-14 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_log', '0002_auto_20210208_2030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ('name', 'transaction_amount'), 'verbose_name': 'Activity', 'verbose_name_plural': 'Activities'},
        ),
        migrations.AlterModelOptions(
            name='activitylog',
            options={'ordering': ('-date', '-time'), 'verbose_name': 'Activity Log', 'verbose_name_plural': 'Activity Logs'},
        ),
        migrations.AlterModelOptions(
            name='activityphotovalidation',
            options={'ordering': ('-activity_log',), 'verbose_name': 'Activity Photo Validation', 'verbose_name_plural': 'Activity Photo Validations'},
        ),
    ]
