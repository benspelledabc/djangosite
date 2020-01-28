import os
import json
from datetime import datetime
from django.conf import settings
from farminvite.models import InviteListing
from .models import WhatIsNew
from django.db.models import Q
from django.db.models import F, ExpressionWrapper
from django.http import JsonResponse


def latest_news():
    this_moment = datetime.now()
    result = WhatIsNew.objects.filter(
        Q(Date=this_moment.date()) |
        Q(Date__lt=this_moment.date())).order_by('-Date', )

    return result


def get_version_json():
    data = open(os.path.join(settings.BASE_DIR, 'release.json')).read()
    json_data = json.loads(data)  # converts to a json structure
    return json_data
