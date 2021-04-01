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
