import json
import datetime
# from datetime import datetime
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import RequestTimeline
from django.db.models import Q, Count
from django.db.models.functions import TruncHour, TruncMonth, TruncYear
from django.db.models.functions import ExtractMonth

from django.contrib.auth.models import User


def requests_by_year():
    result = RequestTimeline.objects.annotate(
        year=TruncYear('request_date')).values('year', ) \
        .annotate(requests_per_year=Count('id')) \
        .order_by('year')

    return result


def requests_by_month():
    result = RequestTimeline.objects\
        .annotate(month=ExtractMonth('request_date')).values("month",)\
        .annotate(requests_per_month=Count('id'))\
        .order_by('month')

    return result


# todo: needs a filter for None|False value... not just an 'else'
def requests_all(request, desired_results="All"):
    if desired_results == "All":
        result = RequestTimeline.objects.all()\
            .order_by('-request_date')
    else:
        result = RequestTimeline.objects.filter(
            Q(received_pa_info_requested=desired_results))\
            .order_by('-request_date')

    # todo: hijack 'received_pa_info_requested' for True|False to Null if 'result_date' is null?

    for item in result:
        if item.result_date is None:
            item.received_pa_info_requested = "Pending Result"
            item.result_date = "Pending Result"

    page = request.GET.get('page', 1)
    paginator = Paginator(result, 5)

    try:
        result_set = paginator.page(page)
    except PageNotAnInteger:
        result_set = paginator.page(1)
    except EmptyPage:
        result_set = paginator.page(paginator.num_pages)

    return result_set
