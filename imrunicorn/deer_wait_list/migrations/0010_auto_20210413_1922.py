# Generated by Django 3.0.7 on 2021-04-13 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deer_wait_list', '0009_auto_20210413_1906'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipient',
            options={'ordering': ('name',), 'permissions': (('view_thankfulness', 'Can View Thankfulness'),)},
        ),
    ]