import os
import json
from datetime import datetime, date, timedelta
from django.conf import settings
from farminvite.models import InviteListing
from .models import WhatIsNew, MainPageBlurbs, PageBlurbOverrides
from django.db.models import Q
from django.db.models import F, ExpressionWrapper
from django.http import JsonResponse


def get_main_page_blurb():
    try:
        blurb = MainPageBlurbs.objects.filter(
            Q(Is_Active=True)
        ).order_by('-id')[:1]
        blurb = blurb[0].Blurb
    except IndexError as ie:
        # blurb = "Blurb Error: %s." % ie
        # give a default
        blurb = "I need a new breakfast."
    except Exception as err:
        blurb = "Blurb Error: %s." % err

    return blurb


def get_restart_notice():
    message = {
        "requested": False,
        "request_time": "never",
        "request_date": "never",
    }
    if os.path.isfile('./admin_toolbox/restart_nginx.token') or \
            os.path.isfile('./admin_toolbox/restart_gunicorn.token'):
        message = {
            "requested": True,
            "request_time": datetime.now() + timedelta(seconds=80),
            "request_date": date.today(),
        }
    return message

# def get_news():
#    this_moment = datetime.now()
#    result = WhatIsNew.objects.filter(
#        Q(Published=True) & (Q(Date=this_moment.date())) |
#        Q(Published=True) & Q(Date__lt=this_moment.date())
#    ).order_by('-Is_Sticky', '-Date', )
#
#    return blurb


def get_page_blurb_override(page=None):
    try:
        blurb = PageBlurbOverrides.objects.filter(
            Q(Page_Link_From_Base=page)
        ).order_by('-id')[:1]
        blurb = blurb[0].Blurb
    except IndexError as ie:
        # blurb = "Blurb Error: %s." % ie
        # give a default
        blurb = ""
    except Exception as err:
        blurb = "Blurb Error: %s." % err

    return blurb


def get_news():
    this_moment = datetime.now()
    result = WhatIsNew.objects.filter(
        Q(Published=True) & (Q(Date=this_moment.date())) |
        Q(Published=True) & Q(Date__lt=this_moment.date())
    ).order_by('-Is_Sticky', '-Date', )

    return result

# It appears i duplicated this code...
# def get_news():
#     this_moment = datetime.now()
#     result = WhatIsNew.objects.filter(
#         Q(Published=True) & (Q(Date=this_moment.date())) |
#         Q(Published=True) & Q(Date__lt=this_moment.date())
#     ).order_by('-Is_Sticky', '-Date', )
#
#     return result


def get_news_by_pk(news_pk='1'):
    result = WhatIsNew.objects.get(pk=news_pk)

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
