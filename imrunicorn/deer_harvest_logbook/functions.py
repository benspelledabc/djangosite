from .models import Harvests
from django.db.models import Q, Count
from django.db.models.functions import TruncHour


def all_harvests():
    result = Harvests.objects.filter()\
        .order_by('-harvest_date', '-harvest_time', '-shot_distance_yards')
    return result


def all_harvests_by_shooter(shooter_pk='1'):
    result = Harvests.objects.filter(
        Q(shooter__pk=shooter_pk)
    ).order_by('-harvest_date', '-harvest_time', '-shot_distance_yards')

    return result


def harvests_by_hour_of_day():
    result = Harvests.objects.annotate(
        hour=TruncHour('harvest_time')).values('hour', ) \
        .annotate(kills_per_hour=Count('id'))\
        .order_by('hour')
    return result


def harvests_by_hour_of_day_by_sex():
    result = Harvests.objects.annotate(
        hour=TruncHour('harvest_time')).values('hour', 'sex',) \
        .annotate(kills_per_hour=Count('id'))\
        .order_by('hour')
    return result


def harvests_by_sex():
    result = Harvests.objects.values('sex', ) \
        .annotate(kills=Count('sex'))\
        .order_by('-kills')
    return result
