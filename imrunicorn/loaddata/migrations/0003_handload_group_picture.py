# Generated by Django 3.0.7 on 2020-10-27 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loaddata', '0002_handload_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='handload',
            name='Group_Picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/load_data/'),
        ),
    ]