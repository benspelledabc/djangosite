# Generated by Django 3.0.7 on 2021-04-30 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_collection', '0024_arduinounosketch'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arduinounosketch',
            options={'ordering': ('-sketch_datetime',), 'verbose_name': 'Arduino Uno Sketch', 'verbose_name_plural': 'Arduino Uno Sketches'},
        ),
    ]
