from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache
import datetime
from imrunicorn import settings
from .functions import unused_function


# class FurTypes(models.Model):
#     name = models.CharField(max_length=150)
#
#     def __str__(self):
#         return "%s" % self.name
#
#
# class Species(models.Model):
#     name = models.CharField(max_length=150)
#     level = models.IntegerField(max_length=2)
#     trophy_score_silver = models.FloatField()
#     trophy_score_gold = models.FloatField()
#     trophy_score_diamond = models.FloatField()
#
#     def __str__(self):
#         return "%s" % self.name


# class ReserveName(models.Model):
#     name = models.CharField(max_length=150)
#
#     def __str__(self):
#         return "%s" % self.name
#
#
# class Species(models.Model):
#     name = models.CharField(max_length=150)
#     reserve_name = models.ForeignKey(ReserveName, default=1, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "%s - %s" % self.name, self.reserve_name
#
#
# class NeedTimes(models.Model):
#     name = models.CharField(max_length=150)
#     reserve_name = models.ForeignKey(ReserveName, default=1, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "%s - %s" % self.name, self.reserve_name
