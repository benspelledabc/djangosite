import json
import datetime
# from datetime import datetime
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import RemovalsByLocation, Location
from django.db.models import Q, Count
from django.db.models.functions import TruncHour, TruncMonth, TruncYear
from django.contrib.auth.models import User


def groundhogs_by_temperature():
    result = RemovalsByLocation.objects.values('estimated_temperature', 'pk') \
        .annotate(kills=Count('estimated_temperature')) \
        .order_by('-estimated_temperature')

    for item in result:
        try:
            temp = item["estimated_temperature"]
            rounded_value = int(round(temp / 5.0) * 5.0)

            # this isn't working so, lets do it this way for now
            if rounded_value != temp:
                update_estimated_temperature(item["pk"], rounded_value)
        except Exception as e:
            print("ERROR: {0}".format(e))

    # fetching again without PK for sorting.
    result = RemovalsByLocation.objects.values('estimated_temperature') \
        .annotate(kills=Count('estimated_temperature')) \
        .order_by('-estimated_temperature')

    return result


def update_estimated_temperature(record_id=1, new_temp=-49):
    try:
        e = RemovalsByLocation.objects.get(id=record_id)
        e.estimated_temperature = new_temp
        e.save()
        print("Record {0} updated to new temperature of {1}.".format(record_id, new_temp))
    except Exception as e:
        print(e)


def groundhogs_by_cloud_level(cloud_level="ALL"):
    # now we're conditionally cloudy
    if cloud_level == "ALL":
        result = RemovalsByLocation.objects.all().count()
    else:
        result = RemovalsByLocation.objects.filter(
            Q(cloud_level=cloud_level)
        ).count()

    print("Level: {0} Result: {1}".format(cloud_level, result))

    return result


def groundhogs_by_month():
    result = RemovalsByLocation.objects.annotate(
        # hour=TruncHour('removal_time')).values('hour', 'sex',) \
        month=TruncMonth('removal_date')).values('month', ) \
        .annotate(kills_per_month=Count('id')) \
        .order_by('month')

    return result


def groundhogs_by_year():
    result = RemovalsByLocation.objects.annotate(
        year=TruncYear('removal_date')).values('year', ) \
        .annotate(kills_per_year=Count('id')) \
        .order_by('year')

    return result


def all_groundhog_hole_locations():
    result = Location.objects.all()
    return result


def all_groundhog_removals(request):
    result = RemovalsByLocation.objects.filter() \
        .order_by('-removal_date', '-removal_time', '-shot_distance_yards')
    page = request.GET.get('page', 1)
    paginator = Paginator(result, 5)

    try:
        result_set = paginator.page(page)
    except PageNotAnInteger:
        result_set = paginator.page(1)
    except EmptyPage:
        result_set = paginator.page(paginator.num_pages)

    return result_set


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
    # print("FUNCTION: {0}".format(result))
    return result


def groundhogs_by_sex():
    result = RemovalsByLocation.objects.values('sex', ) \
        .annotate(kills=Count('sex')) \
        .order_by('-kills')
    return result


def groundhogs_count_by_sex(sex="ALL"):
    # now we're conditionally sexy
    if sex == "ALL":
        result = RemovalsByLocation.objects.all().count()
    else:
        result = RemovalsByLocation.objects.filter(
            Q(sex=sex)
        ).count()

    return result
