from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache
import datetime
from imrunicorn import settings


class UserProfile(models.Model):
    # this causes the harvests to break....
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # instead of 'username' or 'firstname'
    preferred_display_name = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

    # class Meta:
    #     ordering = ('preferred_display_name', '')


class PageCounter(models.Model):
    page_name = models.CharField(max_length=150)
    page_hit_count = models.IntegerField(default=0, null=True)

    def __str__(self):
        return "%s [%s]" % (self.page_name, self.page_hit_count)

    class Meta:
        ordering = ('-page_hit_count', 'page_name')


class PageHideList(models.Model):
    page_name = models.CharField(max_length=150)

    def __str__(self):
        return "%s" % self.page_name

