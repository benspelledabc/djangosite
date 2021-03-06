# Generated by Django 3.0.7 on 2021-01-01 18:32

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farminvite', '0007_auto_20201127_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackingListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Count', models.IntegerField(default=1, null=True, validators=[django.core.validators.MaxValueValidator(9000), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='PackingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('List_Date', models.DateField(default=datetime.date.today)),
                ('Items', models.ManyToManyField(to='farminvite.PackingListItem')),
            ],
        ),
    ]
