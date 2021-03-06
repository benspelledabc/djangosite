import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loaddata', '0002_handload_notes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Harvests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harvest_date', models.DateField(default=datetime.date.today)),
                ('harvest_time', models.TimeField(null=True)),
                ('harvest_score', models.IntegerField(blank=True, null=True)),
                ('bonus_for_not_unpleasant', models.BooleanField(blank=True, default=False, null=True)),
                ('crop_damage_permit', models.BooleanField(blank=True, default=False, null=True)),
                ('estimated_weight_lbs', models.DecimalField(decimal_places=2, default=100.25, max_digits=5)),
                ('shot_distance_yards', models.DecimalField(decimal_places=0, default=200, max_digits=4)),
                ('kill_shot', models.ImageField(blank=True, null=True, upload_to='uploads/deer_shots/')),
                ('kill_shot_two', models.ImageField(blank=True, null=True, upload_to='uploads/deer_shots/')),
                ('extra_info', models.TextField(blank=True, null=True)),
                ('sex', models.CharField(choices=[('UNKNOWN', 'Unknown'), ('MALE', 'Male'), ('FEMALE', 'Female')], default='UNKNOWN', max_length=20)),
                ('firearm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deer_harvest_logbook_firearm', to='loaddata.Firearm')),
                ('load', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deer_harvest_logbook_hand_load', to='loaddata.HandLoad')),
                ('shooter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deer_harvest_logbook_shooter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Harvest',
                'verbose_name_plural': 'Harvests',
                'ordering': ('-harvest_date', 'shooter', 'shot_distance_yards'),
            },
        ),
        migrations.AddConstraint(
            model_name='harvests',
            constraint=models.CheckConstraint(check=models.Q(('harvest_score__gte', 0), ('harvest_score__lte', 6)), name='A harvest score value is valid between 0 and 6'),
        ),
    ]
