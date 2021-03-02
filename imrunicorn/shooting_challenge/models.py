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

    def __str__(self):
        return "%s - %s - %s" % (self.challenge_date, self.title, self.blurb)

    class Meta:
        ordering = ('-challenge_date', '-id')

