# Generated by Django 3.0.7 on 2020-11-27 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farminvite', '0005_invitelisting_paid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invitelisting',
            options={'ordering': ('Invite_Date', '-Paid', 'id')},
        ),
    ]
