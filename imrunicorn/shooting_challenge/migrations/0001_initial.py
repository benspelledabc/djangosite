# Generated by Django 3.0.7 on 2021-03-02 00:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_shot', models.ImageField(blank=True, null=True, upload_to='uploads/shooting_challenge/')),
                ('photo_date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'ordering': ('-photo_date', '-id'),
            },
        ),
        migrations.CreateModel(
            name='ChallengeEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('blurb', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('simple_info', models.TextField(blank=True, null=True)),
                ('challenge_photos', models.ManyToManyField(blank=True, to='shooting_challenge.ChallengePhoto')),
            ],
        ),
    ]