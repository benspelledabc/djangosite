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
    # result = ActivityLog.objects.all() \
    #     .order_by('actor', '-date', '-time', '-activity__transaction_amount')
    result = ActivityLog.objects.filter(approved=True) \
        .order_by('actor', '-date', '-time', '-activity__transaction_amount')

    return result


def activity_photo_validation():
    # result = ActivityPhotoValidation.objects.all() \
    #     .order_by('-activity_log__date', '-activity_log__time')
    result = ActivityPhotoValidation.objects.filter(activity_log__approved=True) \
        .order_by('-activity_log__date', '-activity_log__time')

    return result


def activity_scoreboard_by_user():
    # result = ActivityLog.objects.distinct().values('actor',
    #                                                'actor__userprofile',
    #                                                'actor__userprofile__preferred_display_name',
    #                                                'actor__username',
    #                                                'actor__first_name',
    #                                                'actor__last_name') \
    #     .annotate(points=Sum('activity__transaction_amount')).order_by('-points')
    result = ActivityLog.objects.filter(approved=True).distinct().values('actor',
                                                   'actor__userprofile',
                                                   'actor__userprofile__preferred_display_name',
                                                   'actor__username',
                                                   'actor__first_name',
                                                   'actor__last_name') \
        .annotate(points=Sum('activity__transaction_amount')).order_by('-points')

    return result
