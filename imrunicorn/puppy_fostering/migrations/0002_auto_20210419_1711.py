# Generated by Django 3.0.7 on 2021-04-19 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puppy_fostering', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='momma',
            options={'ordering': ('nickname', 'id'), 'verbose_name': 'Momma', 'verbose_name_plural': 'Mommas'},
        ),
        migrations.AlterModelOptions(
            name='puppy',
            options={'ordering': ('momma__nickname', 'nickname', 'id'), 'verbose_name': 'Puppy', 'verbose_name_plural': 'Puppies'},
        ),
        migrations.AlterModelOptions(
            name='puppynotes',
            options={'ordering': ('puppy', 'note_date'), 'verbose_name': 'Note', 'verbose_name_plural': 'Notes'},
        ),
        migrations.AddField(
            model_name='puppy',
            name='cloud_level',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20),
        ),
    ]