# Generated by Django 3.0.7 on 2020-10-17 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_collection', '0010_auto_20201017_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='picturesforcarousel',
            name='restricted',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
