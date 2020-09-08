# Generated by Django 3.0.3 on 2020-09-08 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deer_wait_list', '0002_requestedorder_choice_cuts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
