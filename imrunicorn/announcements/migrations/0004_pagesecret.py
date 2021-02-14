# Generated by Django 3.0.7 on 2021-02-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0003_auto_20201223_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageSecret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Secret', models.TextField(blank=True, null=True)),
                ('Page_Link_From_Base', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Page Secrets',
                'ordering': ('Page_Link_From_Base', '-id'),
            },
        ),
    ]
