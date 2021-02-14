from django.db import models
from decimal import Decimal
from datetime import date
from enum import Enum


class WhatIsNew(models.Model):
    Date = models.DateField(default=date.today)
    Blurb = models.CharField(max_length=250)
    Body = models.TextField()  # i like big comments...
    Image_One = models.ImageField(upload_to='uploads/announcements/what_is_new/', null=True, blank=True)
    Image_Two = models.ImageField(upload_to='uploads/announcements/what_is_new/', null=True, blank=True)
    Published = models.BooleanField(default=True)
    Is_Sticky = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.Date, self.Blurb)

    class Meta:
        ordering = ('-Is_Sticky', '-Date', 'Blurb')
        verbose_name = 'What Is New'
        verbose_name_plural = 'What Is New'


class MainPageBlurbs(models.Model):
    # Blurb = models.CharField(max_length=250)
    Blurb = models.TextField(blank=True, null=True)  # i like big comments...
    Is_Active = models.BooleanField(default=False)

    def __str__(self):
        return "[%s] - %s" % (self.Is_Active, self.Blurb)

    class Meta:
        ordering = ('-Is_Active', '-id')
        verbose_name_plural = "Main Page Blurbs"


class PageBlurbOverrides(models.Model):
    Blurb = models.CharField(max_length=250)
    Page_Link_From_Base = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return "[%s] - %s" % (self.id, self.Page_Link_From_Base)

    class Meta:
        ordering = ('Page_Link_From_Base', '-id')
        verbose_name_plural = "Page Blurb Overrides"


class PageSecret(models.Model):
    Secret = models.TextField(blank=True, null=True)  # i like big comments...
    Page_Link_From_Base = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return "[%s] - %s" % (self.id, self.Page_Link_From_Base)

    class Meta:
        ordering = ('Page_Link_From_Base', '-id')
        verbose_name_plural = "Page Secrets"
