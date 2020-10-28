import json
import datetime
# from datetime import datetime
from django.conf import settings
from .models import RemovalsByLocation, Location
from django.db.models import Q, Count
from django.db.models.functions import TruncHour
from django.contrib.auth.models import User


def all_groundhog_hole_locations():
    result = Location.objects.all()
    return result


def all_groundhog_removals():
    result = RemovalsByLocation.objects.filter() \
        .order_by('-removal_date', '-removal_time', '-shot_distance_yards')
    return result


def all_groundhog_removals_by_shooter(shooter_pk='1'):
    result = RemovalsByLocation.objects.filter(
        Q(shooter__pk=shooter_pk)
    ).order_by('-removal_date', '-removal_time', '-shot_distance_yards')

    return result


def groundhog_removal_scoreboard():
    result = RemovalsByLocation.objects.distinct().values('shooter',
                                                          'shooter__userprofile',
                                                          'shooter__userprofile__preferred_display_name',
                                                          'shooter__username',
                                                          'shooter__first_name',
                                                          'shooter__last_name') \
                 .annotate(removals=Count('shooter')).order_by('-removals')[:30]

    return result


def groundhog_removal_scoreboard_annual():
    result = RemovalsByLocation.objects.filter(
        removal_date__gte=datetime.datetime.today() -
                          datetime.timedelta(days=366)).distinct().values('shooter',
                                                                          'shooter__userprofile',
                                                                          'shooter__userprofile__preferred_display_name',
                                                                          'shooter__username',
                                                                          'shooter__first_name',
                                                                          'shooter__last_name') \
                 .annotate(removals=Count('shooter')).order_by('-removals')[:30]

    return result


# get the hour portion...
# https://docs.djangoproject.com/en/3.0/ref/models/database-functions/#trunc
# check into lookup, transform, aggregates and be jolly!
def groundhogs_by_hour_of_day():
    result = RemovalsByLocation.objects.annotate(
        # hour=TruncHour('removal_time')).values('hour', 'sex',) \
        hour=TruncHour('removal_time')).values('hour', ) \
        .annotate(kills_per_hour=Count('id')) \
        .order_by('hour')
    return result


def groundhogs_by_hour_of_day_by_sex():
    result = RemovalsByLocation.objects.annotate(
        # hour=TruncHour('removal_time')).values('hour', 'sex',) \
        hour=TruncHour('removal_time')).values('hour', 'sex', ) \
        .annotate(kills_per_hour=Count('id')) \
        .order_by('hour')
    return result


def groundhogs_by_sex():
    result = RemovalsByLocation.objects.values('sex', ) \
        .annotate(kills=Count('sex')) \
        .order_by('-kills')
    return result
