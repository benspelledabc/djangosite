# Generated by Django 3.0.7 on 2020-10-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_collection', '0005_auto_20201017_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='picturesforcarousel',
            name='link_to_external',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]