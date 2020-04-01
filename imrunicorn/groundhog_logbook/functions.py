import json
from datetime import datetime
from django.conf import settings
from .models import RemovalsByLocation, Location
from django.db.models import Q, Count
from django.contrib.auth.models import User


def all_groundhog_hole_locations():
    # this_moment = datetime.now()
    # result = RemovalsByLocation.objects.filter(
    #     Q(Published=True) & (Q(Date=this_moment.date())) |
    #     Q(Published=True) & Q(Date__lt=this_moment.date())
    # ).order_by('-Is_Sticky', '-Date', )

    result = Location.objects.all()

    return result


def all_groundhog_removals():
    # this_moment = datetime.now()
    # result = RemovalsByLocation.objects.filter(
    #     Q(Published=True) & (Q(Date=this_moment.date())) |
    #     Q(Published=True) & Q(Date__lt=this_moment.date())
    # ).order_by('-Is_Sticky', '-Date', )

    # result = RemovalsByLocation.objects.all()
    result = RemovalsByLocation.objects.filter().order_by('-removal_date', '-shot_distance_yards')

    return result


def all_groundhog_removals_by_shooter(shooter_pk='1'):
    # this_moment = datetime.now()
    # result = RemovalsByLocation.objects.filter(
    #     Q(Published=True) & (Q(Date=this_moment.date())) |
    #     Q(Published=True) & Q(Date__lt=this_moment.date())
    # ).order_by('-Is_Sticky', '-Date', )

    # result = RemovalsByLocation.objects.all()
    result = RemovalsByLocation.objects.filter(
        Q(shooter__pk=shooter_pk)
    ).order_by('-removal_date', '-shot_distance_yards')

    return result


def groundhog_removal_scoreboard():
    result = RemovalsByLocation.objects.distinct().values('shooter', 'shooter__username') \
        .annotate(removals=Count('shooter')).order_by('-removals')[:3]
    return result
