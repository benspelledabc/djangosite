from datetime import date
from django.db import models
from loaddata.models import Firearm, HandLoad
from decimal import Decimal
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from imrunicorn.functions import get_weather


class Location(models.Model):
    nickname = models.CharField(max_length=150, default=None, blank=True, null=True)
    # https://viewer.nationalmap.gov/theme/elevation/
    elevation = models.DecimalField(max_digits=5, decimal_places=0, default=764, null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=7, default=39.575230, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=7, default=-76.996040, null=True)

    def get_lat(self):
        return self.latitude

    def get_long(self):
        return self.longitude

    def __str__(self):
        return "%s (%s LAT , %s LONG)" % (self.nickname, self.latitude, self.longitude)

    class Meta:
        ordering = ('nickname', 'latitude', 'longitude')


class RemovalPhoto(models.Model):
    kill_shot = models.ImageField(upload_to='uploads/groundhog_kill_shots/', null=True, blank=True)
    photo_date = models.DateField(default=date.today)

    def __str__(self):
        return "%s - %s - %s" % (self.id, self.photo_date, self.kill_shot.url)

    class Meta:
        ordering = ('-photo_date', '-id')


class RemovalsByLocation(models.Model):
    shooter = models.ForeignKey(User, related_name='groundhog_logbook_shooter', on_delete=models.CASCADE, null=True)
    removal_date = models.DateField(default=date.today)
    removal_time = models.TimeField(null=True)
    estimated_temperature = models.IntegerField(
        null=True,
        default=-49,
        validators=[
            MaxValueValidator(120),
            MinValueValidator(-50)
        ]
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
    wind_dir = models.IntegerField(default=-1)
    wind_dir_word = models.CharField(max_length=40, null=True, blank=True)
    weather_icon_url = models.CharField(max_length=400, null=True, blank=True)
    firearm = models.ForeignKey(Firearm, related_name='groundhog_logbook_firearm', on_delete=models.CASCADE)
    load = models.ForeignKey(HandLoad, related_name='groundhog_logbook_hand_load', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='location', on_delete=models.CASCADE)
    estimated_weight_lbs = models.DecimalField(max_digits=4, decimal_places=2, default=10.25)
    excessive_wound_cavity = models.BooleanField(default=False)
    foot_hold_trapped = models.BooleanField(default=False)
    shot_distance_yards = models.DecimalField(max_digits=4, decimal_places=0, default=200)
    yards_ran = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    extra_info = models.TextField(blank=True, null=True)  # i like big comments...
    # upload the kill shot!?
    kill_shot = models.ImageField(upload_to='uploads/groundhog_kill_shots/', null=True, blank=True)
    kill_shot_two = models.ImageField(upload_to='uploads/groundhog_kill_shots/', null=True, blank=True)

    removal_photos = models.ManyToManyField(RemovalPhoto, blank=True)

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

    def save(self, *args, **kwargs):
        if self.wind_speed == 0.00 and self.wind_dir == -1 and self.estimated_temperature == -49:
            # only fetch weather if it appears to be defaults
            # weather = get_weather(self)
            weather = get_weather(self, self.location.latitude, self.location.longitude)
            self.estimated_temperature = weather['temperature']
            self.cloud_level = weather['description']
            self.wind_speed = weather['wind_speed']
            self.wind_dir = weather['wind_dir']
            self.wind_dir_word = weather['wind_dir_word']
            self.weather_icon_url = weather['weather_icon_url']
        super(RemovalsByLocation, self).save(*args, **kwargs)

    def __str__(self):
        name = self.shooter
        try:
            name = self.shooter.userprofile.preferred_display_name
        except Exception as e:
            name = self.shooter
        return "%s - %s (%s yards from '%s')" % (self.removal_date,
                                                 name,
                                                 self.shot_distance_yards,
                                                 self.location.nickname)

    class Meta:
        # shooter__userprofile__preferred_display_name
        ordering = ('-removal_date', 'shooter', 'shot_distance_yards')

