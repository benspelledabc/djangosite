# Generated by Django 3.0.7 on 2021-04-27 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_collection', '0022_auto_20210416_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorReadings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_datetime', models.DateTimeField(auto_now_add=True)),
                ('sensor_location', models.CharField(max_length=150)),
                ('sensor_model', models.CharField(default='DHT22', max_length=150)),
                ('celsius', models.DecimalField(decimal_places=2, default=1.21, max_digits=5)),
                ('fahrenheit', models.DecimalField(decimal_places=2, default=5.56, max_digits=5)),
                ('humidity', models.DecimalField(decimal_places=2, default=7.62, max_digits=4)),
            ],
            options={
                'verbose_name': 'Sensor Reading',
                'verbose_name_plural': 'Sensor Readings',
                'ordering': ('-read_datetime',),
            },
        ),
    ]