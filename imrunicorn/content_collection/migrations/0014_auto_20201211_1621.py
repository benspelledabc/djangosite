# Generated by Django 3.0.7 on 2020-12-11 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_collection', '0013_fantasygrounds'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='danddfiftheditionbook',
            options={'ordering': ('-pk', 'file_title', 'file_name')},
        ),
        migrations.RemoveField(
            model_name='danddfiftheditionbook',
            name='restricted',
        ),
    ]