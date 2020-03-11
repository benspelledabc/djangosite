from django.db import models
from decimal import Decimal
from datetime import date
from enum import Enum


class WhatIsNew(models.Model):
    Date = models.DateField(default=date.today)
    Blurb = models.CharField(max_length=250)
    Body = models.TextField()  # i like big comments...
    Published = models.BooleanField(default=True)
    Is_Sticky = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.Date, self.Blurb)

    class Meta:
        ordering = ('-Date', 'Blurb')
        verbose_name = 'What Is New'
        verbose_name_plural = 'What Is New'
