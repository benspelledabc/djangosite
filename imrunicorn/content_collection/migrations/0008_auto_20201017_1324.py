# Generated by Django 3.0.7 on 2020-10-17 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_collection', '0007_auto_20201017_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturesforcarousel',
            name='caption',
            field=models.CharField(blank='no name yet', default='no name yet', max_length=250, null='no name yet'),
        ),
    ]
