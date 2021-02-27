from .models import Harvests
from django.db.models import Q, Count
from django.db.models.functions import TruncHour
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.functions import TruncHour, TruncMonth, TruncYear


def all_harvests(request):
    result = Harvests.objects.filter() \
        .order_by('-harvest_date', '-harvest_time', '-shot_distance_yards')
    page = request.GET.get('page', 1)
    paginator = Paginator(result, 5)

    try:
        result_set = paginator.page(page)
    except PageNotAnInteger:
        result_set = paginator.page(1)
    except EmptyPage:
        result_set = paginator.page(paginator.num_pages)

    return result_set


def all_harvests_by_shooter(shooter_pk='1'):
    result = Harvests.objects.filter(
        Q(shooter__pk=shooter_pk)
    ).order_by('-harvest_date', '-harvest_time', '-shot_distance_yards')

    return result


def harvests_by_hour_of_day():
    result = Harvests.objects.annotate(
        hour=TruncHour('harvest_time')).values('hour', ) \
        .annotate(kills_per_hour=Count('id')) \
        .order_by('hour')
    return result


def harvests_by_score():
    result = Harvests.objects.values('harvest_score', ) \
        .annotate(kills_per_hour=Count('id')) \
        .order_by('-harvest_score')
    return result


def harvests_count_by_sex(sex="ALL"):
    result = Harvests.objects.values('sex', ) \
        .annotate(kills=Count('sex')) \
        .order_by('-kills')
    return result


def harvests_by_sex(sex="ALL"):
    # now we're conditionally sexy
    if sex == "ALL":
        result = Harvests.objects.all().count()
    else:
        result = Harvests.objects.filter(
            Q(sex=sex)
        ).count()

    return result


def harvests_by_month():
    result = Harvests.objects.annotate(
        month=TruncMonth('harvest_date')).values('month', ) \
        .annotate(kills_per_month=Count('id')) \
        .order_by('month')

    return result


def harvests_by_year():
    result = Harvests.objects.annotate(
        year=TruncYear('harvest_date')).values('year', ) \
        .annotate(kills_per_year=Count('id')) \
        .order_by('year')

    return result


def harvests_scoreboard():
    result = Harvests.objects.distinct().values('shooter',
                                                'shooter__userprofile',
                                                'shooter__userprofile__preferred_display_name',
                                                'shooter__username',
                                                'shooter__first_name',
                                                'shooter__last_name') \
                 .annotate(removals=Count('shooter')).order_by('-removals')[:30]

    return result


def update_estimated_temperature(record_id=1, new_temp=-49):
    try:
        e = Harvests.objects.get(id=record_id)
        e.estimated_temperature = new_temp
        e.save()
        # print("Record {0} updated to new temperature of {1}.".format(record_id, new_temp))
    except Exception as e:
        print(e)


def harvests_by_temperature():
    result = Harvests.objects.values('estimated_temperature', 'pk') \
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
    result = Harvests.objects.values('estimated_temperature') \
        .annotate(kills=Count('estimated_temperature')) \
        .order_by('-estimated_temperature')

    return result


def harvests_by_cloud_level(cloud_level="ALL"):
    # now we're conditionally cloudy
    if cloud_level == "ALL":
        result = Harvests.objects.all().count()
    else:
        result = Harvests.objects.filter(
            Q(cloud_level=cloud_level)
        ).count()

    return result


# def harvests_by_shooter(shooter_pk='1'):
#     result = Harvests.objects.filter(
#         Q(shooter__pk=shooter_pk)
#     ).order_by('-harvest_date', '-harvest_time')
#
#     return result
