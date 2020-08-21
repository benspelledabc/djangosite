# -*- coding: utf-8 -*-
from django.http import HttpRequest
from django.db import models
from datetime import date, datetime


class Poll(models.Model):
    question = models.CharField(max_length=200)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    reference_link = models.CharField(max_length=450, default=None, blank=True, null=True)

    def __str__(self):              # Python 3: def __unicode__(self):
        return self.question

    class Meta:
        ordering = ('-end_date', 'start_date')


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):              # Python 3: def __unicode__(self):
        return self.choice_text
