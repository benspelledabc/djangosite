# Generated by Django 3.0.7 on 2021-03-21 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_collection', '0017_randominsult'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='randominsult',
            options={'ordering': ('-pk', 'insult'), 'verbose_name': 'Random Insult', 'verbose_name_plural': 'Random Insults'},
        ),
        migrations.RenameField(
            model_name='randominsult',
            old_name='file_title',
            new_name='insult',
        ),
    ]