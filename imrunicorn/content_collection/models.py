from datetime import datetime, date
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class Video(models.Model):
    file_title = models.CharField(max_length=150, default=None, blank=True, null=True)
    file_name = models.FileField(upload_to='uploads/content_collection/videos/', null=True, blank=True)
    restricted = models.BooleanField(default=True, null=True)

    def __str__(self):
        return "#%s - [%s] %s (%s)" % (self.pk, self.restricted, self.file_title, self.file_name)

    class Meta:
        ordering = ('-pk', 'restricted', 'file_title', 'file_name')


class PicturesForCarousel(models.Model):
    caption = models.CharField(max_length=250, null="no name yet", blank="no name yet", default="no name yet")
    picture = models.ImageField(upload_to='uploads/carousel/', null=True, blank=True)
    link_to_external = models.CharField(max_length=250, null=True, blank=True)
    restricted = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ('-pk', 'caption')
        verbose_name = 'Picture For Carousel'
        verbose_name_plural = 'Pictures For Carousel'


class DAndDFifthEditionBook(models.Model):
    file_title = models.CharField(max_length=150, default=None, blank=True, null=True)
    file_name = models.FileField(upload_to='uploads/content_collection/dnd5e_books/', null=True, blank=True)
    restricted = models.BooleanField(default=True, null=True)

    def __str__(self):
        return "#%s [%s]- %s (%s)" % (self.pk, self.restricted, self.file_title, self.file_name)

    class Meta:
        ordering = ('-pk', 'file_title', 'file_name')
        verbose_name = 'D & D 5th Edition Book'
        verbose_name_plural = 'D & D 5th Edition Book'


class FantasyGrounds(models.Model):
    file_title = models.CharField(max_length=150, default=None, blank=True, null=True)
    file_name = models.FileField(upload_to='uploads/content_collection/FantasyGrounds/', null=True, blank=True)

    def __str__(self):
        return "#%s - %s (%s)" % (self.pk, self.file_title, self.file_name)

    class Meta:
        ordering = ('-pk', 'file_title', 'file_name')
        verbose_name = 'Fantasy Grounds'
        verbose_name_plural = 'Fantasy Grounds'


class RandomInsult(models.Model):
    insult = models.TextField(unique=True, blank=True, null=True)  # i like big comments...

    def __str__(self):
        return "[%s] %s" % (self.pk, self.insult)

    class Meta:
        ordering = ('-pk', 'insult')
        verbose_name = 'Random Insult'
        verbose_name_plural = 'Random Insults'


class Secret(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField(blank=True, null=True)  # i like big comments...

    def __str__(self):
        return "[%s] %s" % (self.pk, self.title)

    class Meta:
        ordering = ('-pk', )
        verbose_name = 'Secret'
        verbose_name_plural = 'Secrets'


class BuzzWordOrPhrase(models.Model):
    word_or_phrase = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return "[%s] %s" % (self.pk, self.word_or_phrase)

    class Meta:
        ordering = ('-pk', )
        verbose_name = 'Buzzword or Phrase'
        verbose_name_plural = 'Buzzwords or Phrases'


class SensorReadings(models.Model):
    read_datetime = models.DateTimeField(auto_now_add=True, blank=True)
    sensor_location = models.CharField(max_length=150)
    sensor_model = models.CharField(max_length=150, default="DHT22")
    celsius = models.DecimalField(max_digits=5, decimal_places=2, default=1.21)
    fahrenheit = models.DecimalField(max_digits=5, decimal_places=2, default=5.56)
    humidity = models.DecimalField(max_digits=4, decimal_places=2, default=7.62)

    def __str__(self):
        return "%s - %s" % (self.read_datetime, self.sensor_location)

    class Meta:
        ordering = ('-read_datetime', )
        verbose_name = 'Sensor Reading'
        verbose_name_plural = 'Sensor Readings'
