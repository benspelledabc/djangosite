import json
from datetime import datetime
from django.conf import settings
from .models import RemovalsByLocation, Location
from django.db.models import Q, Count
from django.contrib.auth.models import User


def all_groundhog_hole_locations():
    result = Location.objects.all()
    return result


def all_groundhog_removals():
    result = RemovalsByLocation.objects.filter().order_by('-removal_date', '-shot_distance_yards')
    return result


def all_groundhog_removals_by_shooter(shooter_pk='1'):
    result = RemovalsByLocation.objects.filter(
        Q(shooter__pk=shooter_pk)
    ).order_by('-removal_date', '-shot_distance_yards')

    return result


def groundhog_removal_scoreboard():
    result = RemovalsByLocation.objects.distinct().values('shooter', 'shooter__username') \
        .annotate(removals=Count('shooter')).order_by('-removals')[:3]
    return result


def groundhogs_by_hour_of_day():
    result = RemovalsByLocation.objects.distinct().values('sex', 'removal_time') \
        .annotate(removals=Count('sex')).order_by('removal_time')
    return result
