import os
import json
from datetime import datetime
from django.conf import settings
from farminvite.models import InviteListing
from .models import WhatIsNew
from django.db.models import Q
from django.db.models import F, ExpressionWrapper
from django.http import JsonResponse


def get_news():
    this_moment = datetime.now()
    result = WhatIsNew.objects.filter(
        Q(Published=True) & (Q(Date=this_moment.date())) |
        Q(Published=True) & Q(Date__lt=this_moment.date())
    ).order_by('-Is_Sticky', '-Date', )

    return result


# last 5 posts, sticky first.
def get_news_sticky():
    this_moment = datetime.now()
    result = WhatIsNew.objects.filter(
        Q(Published=True) & (Q(Date=this_moment.date())) |
        Q(Published=True) & Q(Date__lt=this_moment.date())
    ).order_by('-Is_Sticky', '-Date')[:7]

    return result


def get_version_json():
    data = open(os.path.join(settings.BASE_DIR, 'release.json')).read()
    json_data = json.loads(data)  # converts to a json structure
    return json_data
