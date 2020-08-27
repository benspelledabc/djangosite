from django.db import models
from datetime import date
from django.db import models
from loaddata.models import Firearm, HandLoad
from decimal import Decimal
from django.contrib.auth.models import User


# Create your models here.

class Harvests(models.Model):
    shooter = models.ForeignKey(User, related_name='deer_harvest_logbook_shooter', on_delete=models.CASCADE, null=True)
    harvest_date = models.DateField(default=date.today)
    harvest_time = models.TimeField(null=True)
    firearm = models.ForeignKey(Firearm, related_name='deer_harvest_logbook_firearm', on_delete=models.CASCADE)
    load = models.ForeignKey(HandLoad, related_name='deer_harvest_logbook_hand_load', on_delete=models.CASCADE)
    estimated_weight_lbs = models.DecimalField(max_digits=5, decimal_places=2, default=100.25)
    # excessive_wound_cavity = models.BooleanField(default=False)
    shot_distance_yards = models.DecimalField(max_digits=4, decimal_places=0, default=200)
    kill_shot = models.ImageField(upload_to='uploads/deer_shots/', null=True, blank=True)
    kill_shot_two = models.ImageField(upload_to='uploads/deer_shots/', null=True, blank=True)
    extra_info = models.TextField(blank=True, null=True)  # i like big comments...

    UNKNOWN = 'UNKNOWN'
    MALE = 'MALE'
    FEMALE = 'FEMALE'

    SEX_CHOICES = [
        (UNKNOWN, 'Unknown'),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    sex = models.CharField(
        max_length=20,
        choices=SEX_CHOICES,
        default=UNKNOWN,
    )

    def __str__(self):
        return "%s - %s (%s yards from '%s')" % (self.harvest_date,
                                                 self.shooter,
                                                 self.shot_distance_yards,
                                                 self.estimated_weight_lbs)

    class Meta:
        ordering = ('-harvest_date', 'shooter', 'shot_distance_yards')

