# Generated by Django 3.0.7 on 2020-11-22 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farminvite', '0002_auto_20201122_1811'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invitelisting',
            options={'ordering': ('Invite_Date', 'Invite_Secondary', 'Invite_Display_Name', 'Phone_Number')},
        ),
        migrations.RenameField(
            model_name='invitelisting',
            old_name='MDShooters_Name',
            new_name='Invite_Display_Name',
        ),
    ]
