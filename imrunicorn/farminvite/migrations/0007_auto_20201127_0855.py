# Generated by Django 3.0.7 on 2020-11-27 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farminvite', '0006_auto_20201127_0838'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invitelisting',
            options={'ordering': ('-Paid', 'id', 'Invite_Date')},
        ),
    ]
