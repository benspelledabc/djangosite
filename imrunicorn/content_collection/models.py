from django.db import models
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

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ('caption', '-pk')

