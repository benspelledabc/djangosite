from datetime import date
from loaddata.models import Firearm, HandLoad
from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User


class Location(models.Model):
    nickname = models.CharField(max_length=150, default=None, blank=True, null=True)
    # https://viewer.nationalmap.gov/theme/elevation/
    elevation = models.DecimalField(max_digits=5, decimal_places=0, default=764, null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=7, default=39.575230, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=7, default=-76.996040, null=True)

    def __str__(self):
        return "%s (%s , %s)" % (self.nickname, self.latitude, self.longitude)

    class Meta:
        ordering = ('latitude', 'nickname')


class ShotCollection(models.Model):
    shooter = models.ForeignKey(User, related_name='shooter', on_delete=models.CASCADE, null=True)
    collection_date = models.DateField(default=date.today)
    # location = models.CharField(max_length=150, default=None, blank=True, null=True)
    location = models.ForeignKey(Location, related_name='shot_collection_location', on_delete=models.CASCADE, null=True)
    firearm = models.ForeignKey(Firearm, related_name='shot_collection_firearm', on_delete=models.CASCADE, null=True)
    load = models.ForeignKey(HandLoad, related_name='shot_collection_hand_load', on_delete=models.CASCADE, null=True)

    notes = models.TextField(blank=True, null=True)  # i like big comments...

    def __str__(self):
        return "%s %s @ %s [Using: %s]" % (self.collection_date, self.shooter, self.location, self.load)

    class Meta:
        ordering = ('shooter', 'collection_date')


class ShotEntry(models.Model):
    NONE = 'NONE'
    LIGHT = 'LIGHT'
    MODERATE = 'MODERATE'
    HEAVY = 'HEAVY'
    OTHER = 'OTHER'

    WIND_SPEED_CHOICES = [
        (NONE, 'no wind'),
        (LIGHT, '0-5 MPH wind'),
        (MODERATE, '6-10 MPH wind'),
        (HEAVY, '11-15 MPH wind'),
        (OTHER, '16+ MPH wind'),
    ]

    NO_VALUE_TOWARD = 'NO_VALUE_TOWARD'
    NO_VALUE_BEHIND = 'NO_VALUE_BEHIND'
    HALF_VALUE_TOWARD = 'HALF_VALUE_TOWARD'
    HALF_VALUE_BEHIND = 'HALF_VALUE_BEHIND'
    FULL_VALUE_ACROSS = 'FULL_VALUE_ACROSS'

    WIND_VALUE_CHOICES = [
        (NO_VALUE_TOWARD, 'No Value (toward)'),
        (NO_VALUE_BEHIND, 'No Value (behind)'),
        (HALF_VALUE_TOWARD, '1/2 Value (toward)'),
        (HALF_VALUE_BEHIND, '1/2 Value (behind)'),
        (FULL_VALUE_ACROSS, 'Full Value (across)'),
    ]

    collection = models.ForeignKey(ShotCollection, related_name='shot_collection', on_delete=models.CASCADE, null=True)
    shotNumber = models.IntegerField(null=True)
    wind_speed = models.CharField(
        max_length=20,
        choices=WIND_SPEED_CHOICES,
        default=LIGHT,
    )

    wind_direction = models.CharField(
        max_length=30,
        choices=WIND_VALUE_CHOICES,
        default=NO_VALUE_BEHIND,
    )

    def __str__(self):
        return "%s - Shot: %s" % (self.collection, self.shotNumber)

    class Meta:
        ordering = ('collection', 'shotNumber',)

