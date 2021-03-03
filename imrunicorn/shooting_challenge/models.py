from datetime import date
from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from imrunicorn.functions import get_weather


class ChallengePhoto(models.Model):
    challenge_shot = models.ImageField(upload_to='uploads/shooting_challenge/', null=True, blank=True)
    photo_date = models.DateField(default=date.today)

    def __str__(self):
        return "%s - %s - %s" % (self.id, self.photo_date, self.challenge_shot.url)

    class Meta:
        ordering = ('-photo_date', '-id')


class ChallengeEvent(models.Model):
    challenge_date = models.DateField(default=date.today)
    title = models.CharField(max_length=150, default=None, blank=True, null=True)
    blurb = models.CharField(max_length=150, default=None, blank=True, null=True)
    simple_info = models.TextField(blank=True, null=True)  # i like big comments...
    challenge_photos = models.ManyToManyField(ChallengePhoto, blank=True)
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
    wind_dir = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        if self.wind_speed == 0.00 and self.wind_dir == 1 and self.estimated_temperature == -49:
            # only fetch weather if it appears to be defaults
            weather = get_weather(self)
            self.estimated_temperature = weather['temperature']
            self.cloud_level = weather['description']
            self.wind_speed = weather['wind_speed']
            self.wind_dir = weather['wind_dir']
        super(ChallengeEvent, self).save(*args, **kwargs)

    def __str__(self):
        return "%s - %s - %s" % (self.challenge_date, self.title, self.blurb)

    class Meta:
        ordering = ('-challenge_date', '-id')

