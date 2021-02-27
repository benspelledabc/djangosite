from .models import Harvests
from django.db.models import Q, Count
from django.db.models.functions import TruncHour
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def all_harvests(request):
    result = Harvests.objects.filter()\
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
        .annotate(kills_per_hour=Count('id'))\
        .order_by('hour')
    return result


def harvests_by_score():
    result = Harvests.objects.values('harvest_score', ) \
        .annotate(kills_per_hour=Count('id'))\
        .order_by('-harvest_score')
    return result


def harvests_by_sex():
    result = Harvests.objects.values('sex', ) \
        .annotate(kills=Count('sex'))\
        .order_by('-kills')
    return result
