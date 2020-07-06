from datetime import date
from django.db import models
from loaddata.models import Firearm, HandLoad
from decimal import Decimal
from django.contrib.auth.models import User


class Location(models.Model):
    nickname = models.CharField(max_length=150, default=None, blank=True, null=True)
    # https://viewer.nationalmap.gov/theme/elevation/
    elevation = models.DecimalField(max_digits=5, decimal_places=0, default=764, null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=7, default=39.575230, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=7, default=-76.996040, null=True)

    def __str__(self):
        return "%s (%s LAT , %s LONG)" % (self.nickname, self.latitude, self.longitude)

    class Meta:
        ordering = ('nickname', 'latitude', 'longitude')


class RemovalsByLocation(models.Model):
    shooter = models.ForeignKey(User, related_name='groundhog_logbook_shooter', on_delete=models.CASCADE, null=True)
    removal_date = models.DateField(default=date.today)
    removal_time = models.TimeField(null=True)
    firearm = models.ForeignKey(Firearm, related_name='groundhog_logbook_firearm', on_delete=models.CASCADE)
    load = models.ForeignKey(HandLoad, related_name='groundhog_logbook_hand_load', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='location', on_delete=models.CASCADE)
    estimated_weight_lbs = models.DecimalField(max_digits=4, decimal_places=2, default=10.25)
    excessive_wound_cavity = models.BooleanField(default=False)
    shot_distance_yards = models.DecimalField(max_digits=4, decimal_places=0, default=200)
    extra_info = models.TextField(blank=True, null=True)  # i like big comments...
    # upload the kill shot!?
    kill_shot = models.ImageField(upload_to='uploads/groundhog_kill_shots/', null=True, blank=True)
    kill_shot_two = models.ImageField(upload_to='uploads/groundhog_kill_shots/', null=True, blank=True)

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
        return "%s - %s (%s yards from '%s')" % (self.removal_date,
                                                 self.shooter,
                                                 self.shot_distance_yards,
                                                 self.location.nickname)

    class Meta:
        ordering = ('removal_date', 'shooter', 'shot_distance_yards')

