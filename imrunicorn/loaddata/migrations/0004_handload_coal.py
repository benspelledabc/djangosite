# Generated by Django 3.0.7 on 2020-12-28 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loaddata', '0003_handload_group_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='handload',
            name='COAL',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
    ]
