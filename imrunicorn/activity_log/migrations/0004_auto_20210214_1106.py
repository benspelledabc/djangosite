# Generated by Django 3.0.7 on 2021-02-14 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_log', '0003_auto_20210213_2304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ('-transaction_amount', 'name'), 'verbose_name': 'Activity', 'verbose_name_plural': 'Activities'},
        ),
    ]
