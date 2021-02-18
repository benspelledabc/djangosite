import json
import datetime
# from datetime import datetime
from django.conf import settings
from .models import Activity, ActivityLog, ActivityPhotoValidation
from django.db.models import Q, Count, Sum
from django.db.models.functions import TruncHour, TruncMonth, TruncYear
from django.contrib.auth.models import User


def activity_scoreboard():
    result = {
        "username": "sample",
        "points": 43
    }

    return result


def activity_list():
    result = Activity.objects.all().order_by('-transaction_amount')

    return result


def activity_tasks_per_user():
    result = ActivityLog.objects.all() \
        .order_by('actor', '-activity__transaction_amount', '-date', '-time')

    # for item in result:
    #     print("{0} - {1} - {2}".format(item.activity.transaction_amount, item.actor.username, item.activity.name))
    #     print("{0} - {1} -- {2} {3}".format(item.date, item.time, item.actor.username, item.activity.name))

    return result


def activity_photo_validation():
    result = ActivityPhotoValidation.objects.all() \
        .order_by('-activity_log__date', '-activity_log__time')

    return result


def activity_scoreboard_by_user():
    result = ActivityLog.objects.distinct().values('actor') \
        .annotate(points=Sum('activity__transaction_amount')).order_by('-points')
    # <QuerySet [{'actor': 1, 'points': 27}, {'actor': 2, 'points': 5}]>
    # print(result)

    return result
