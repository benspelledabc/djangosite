# Generated by Django 3.0.7 on 2020-10-17 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_collection', '0006_picturesforcarousel_link_to_external'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturesforcarousel',
            name='caption',
            field=models.CharField(blank='no name yet', max_length=250, null='no name yet'),
        ),
    ]
