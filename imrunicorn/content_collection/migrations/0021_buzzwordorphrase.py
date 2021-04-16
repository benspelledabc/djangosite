# Generated by Django 3.0.7 on 2021-04-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_collection', '0020_secret'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuzzWordOrPhrase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_or_phrase', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Buzzword or Phrase',
                'verbose_name_plural': 'Buzzwords or Phrases',
                'ordering': ('-pk',),
            },
        ),
    ]