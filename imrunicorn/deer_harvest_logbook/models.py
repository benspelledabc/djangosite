from django.db import models
from datetime import date
from django.db import models
from loaddata.models import Firearm, HandLoad
from decimal import Decimal
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from imrunicorn.functions import get_weather


# Create your models here.


class HarvestPhoto(models.Model):
    kill_shot = models.ImageField(upload_to='uploads/deer_shots/', null=True, blank=True)
    photo_date = models.DateField(default=date.today)

    def __str__(self):
        return "%s - %s - %s" % (self.id, self.photo_date, self.kill_shot.url)

    class Meta:
        ordering = ('-photo_date', '-id')


class DeerManagementPermit(models.Model):
    issued_to = models.ForeignKey(User, on_delete=models.CASCADE)
    permit_id = models.CharField(max_length=10, default='06375')

    def __str__(self):
        return "%s - %s" % (self.issued_to, self.permit_id)

    class Meta:
        ordering = ('permit_id', )


class Harvests(models.Model):
    shooter = models.ForeignKey(User, related_name='deer_harvest_logbook_shooter', on_delete=models.CASCADE, null=True)
    harvest_date = models.DateField(default=date.today)
    harvest_time = models.TimeField(null=True)
    dnr_confirmation = models.CharField(blank=True, default=None, max_length=50, null=True)
    harvest_score = models.IntegerField(null=True, blank=True)
    bonus_for_not_unpleasant = models.BooleanField(default=False, null=True, blank=True)
    # crop_damage_permit = models.BooleanField(default=False, null=True, blank=True)
    deer_management_permit_id = models.ForeignKey(DeerManagementPermit, on_delete=models.CASCADE, null=True, blank=True)
    firearm = models.ForeignKey(Firearm, related_name='deer_harvest_logbook_firearm', on_delete=models.CASCADE)
    load = models.ForeignKey(HandLoad, related_name='deer_harvest_logbook_hand_load', on_delete=models.CASCADE)
    estimated_weight_lbs = models.DecimalField(max_digits=5, decimal_places=2, default=100.25)
    # excessive_wound_cavity = models.BooleanField(default=False)
    shot_distance_yards = models.DecimalField(max_digits=4, decimal_places=0, default=200)
    yards_ran = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    extra_info = models.TextField(blank=True, null=True)  # i like big comments...
    kill_shot = models.ImageField(upload_to='uploads/deer_shots/', null=True, blank=True)
    kill_shot_two = models.ImageField(upload_to='uploads/deer_shots/', null=True, blank=True)
    removal_photos = models.ManyToManyField(HarvestPhoto, blank=True)

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

    CLEAR_SKY = 'Clear Sky'
    FEW_CLOUDS = 'Few Clouds'
    SCATTERED_CLOUDS = 'Scattered Clouds'
    BROKEN_CLOUDS = 'Broken Clouds'
    SHOWER_RAIN = "Shower/Rain"
    RAIN = "Rain"
    THUNDERSTORM = "Thunderstorm"
    SNOW = "Snow"
    MIST = "Mist"
    UNKNOWN = 'Unknown'

    cloud_level_choices = [
        (CLEAR_SKY, 'Clear Sky'),
        (FEW_CLOUDS, 'Few Clouds'),
        (SCATTERED_CLOUDS, 'Scattered Clouds'),
        (BROKEN_CLOUDS, 'Broken Clouds'),
        (SHOWER_RAIN, 'Shower/Rain'),
        (RAIN, 'Rain'),
        (THUNDERSTORM, 'Thunderstorm'),
        (SNOW, 'Snow'),
        (MIST, 'Mist'),
        (UNKNOWN, 'Unknown'),
    ]
    cloud_level = models.CharField(
        max_length=20,
        choices=cloud_level_choices,
        default=UNKNOWN,
    )
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    wind_dir = models.IntegerField(default=1)
    estimated_temperature = models.IntegerField(
        null=True,
        default=-49,
        validators=[
            MaxValueValidator(120),
            MinValueValidator(-50)
        ]
    )

    def save(self, *args, **kwargs):
        if self.wind_speed == 0.00 and self.wind_dir == 1 and self.estimated_temperature == -49:
            # only fetch weather if it appears to be defaults
            weather = get_weather(self, 39.619718, -77.023989)
            # weather = get_weather(self, self.location.latitude, self.location.longitude)
            self.estimated_temperature = weather['temperature']
            self.cloud_level = weather['description']
            self.wind_speed = weather['wind_speed']
            self.wind_dir = weather['wind_dir']
        super(Harvests, self).save(*args, **kwargs)

    def __str__(self):
        return "%s - %s (%s yards from '%s')" % (self.harvest_date,
                                                 self.shooter,
                                                 self.shot_distance_yards,
                                                 self.estimated_weight_lbs)

    class Meta:
        verbose_name = 'Harvest'
        verbose_name_plural = 'Harvests'
        ordering = ('-harvest_date', '-harvest_time', 'shooter', 'shot_distance_yards')


