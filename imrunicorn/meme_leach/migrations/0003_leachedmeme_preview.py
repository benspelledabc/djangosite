# Generated by Django 3.0.7 on 2021-04-30 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meme_leach', '0002_remove_leachedmeme_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='leachedmeme',
            name='preview',
            field=models.ManyToManyField(blank=True, to='meme_leach.LeachedMemePreview'),
        ),
    ]