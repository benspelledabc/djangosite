# Generated by Django 3.0.3 on 2020-08-21 03:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestartRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(default=datetime.date.today)),
                ('request_time', models.TimeField(null=True)),
                ('restart_gunicorn', models.BooleanField(default=True)),
                ('restart_nginx', models.BooleanField(default=True)),
                ('request_cancel', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Restart Requests',
                'verbose_name_plural': 'Restart Requests',
                'ordering': ('-request_date', '-request_time'),
            },
        ),
    ]
