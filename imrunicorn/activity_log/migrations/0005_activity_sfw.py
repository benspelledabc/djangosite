# Generated by Django 3.0.7 on 2021-02-16 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_log', '0004_auto_20210214_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='sfw',
            field=models.BooleanField(default=False),
        ),
    ]
