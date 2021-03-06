# Generated by Django 3.0.3 on 2020-08-26 22:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loaddata', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('elevation', models.DecimalField(decimal_places=0, default=764, max_digits=5, null=True)),
                ('latitude', models.DecimalField(decimal_places=7, default=39.57523, max_digits=12, null=True)),
                ('longitude', models.DecimalField(decimal_places=7, default=-76.99604, max_digits=12, null=True)),
            ],
            options={
                'ordering': ('nickname', 'latitude', 'longitude'),
            },
        ),
        migrations.CreateModel(
            name='RemovalsByLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('removal_date', models.DateField(default=datetime.date.today)),
                ('removal_time', models.TimeField(null=True)),
                ('estimated_weight_lbs', models.DecimalField(decimal_places=2, default=10.25, max_digits=4)),
                ('excessive_wound_cavity', models.BooleanField(default=False)),
                ('shot_distance_yards', models.DecimalField(decimal_places=0, default=200, max_digits=4)),
                ('extra_info', models.TextField(blank=True, null=True)),
                ('kill_shot', models.ImageField(blank=True, null=True, upload_to='uploads/groundhog_kill_shots/')),
                ('kill_shot_two', models.ImageField(blank=True, null=True, upload_to='uploads/groundhog_kill_shots/')),
                ('kill_shot_three', models.ImageField(blank=True, null=True, upload_to='uploads/groundhog_kill_shots/')),
                ('sex', models.CharField(choices=[('UNKNOWN', 'Unknown'), ('MALE', 'Male'), ('FEMALE', 'Female')], default='UNKNOWN', max_length=20)),
                ('firearm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groundhog_logbook_firearm', to='loaddata.Firearm')),
                ('load', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groundhog_logbook_hand_load', to='loaddata.HandLoad')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='groundhog_logbook.Location')),
                ('shooter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='groundhog_logbook_shooter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-removal_date', 'shooter', 'shot_distance_yards'),
            },
        ),
    ]
