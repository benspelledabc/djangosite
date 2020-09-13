import os
import json
from datetime import datetime, date, timedelta
from .models import WatchItem
from django.conf import settings
from django.db.models import Q
from django.db.models import F, ExpressionWrapper
from django.http import JsonResponse

# https://stackoverflow.com/questions/29068275/execute-django-shell-command-as-cron


def get_watch_list():
    this_moment = datetime.now()
    result = WatchItem.objects.all()\
        .order_by('-item_phrase_not_exist')

    return result
