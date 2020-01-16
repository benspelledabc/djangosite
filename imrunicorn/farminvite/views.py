import json
import os
from datetime import datetime
from django.conf import settings
from django.db.models import Q
from django.db.models import F, ExpressionWrapper
from django.http import JsonResponse
from django.shortcuts import render
from model_utils.models import now

from .models import InviteListing


# Create your views here.


def get_version_json(request):
    # data = open('release.json').read()  # opens the json file and saves the raw contents
    data = open(os.path.join(settings.BASE_DIR, 'release.json')).read()
    json_data = json.loads(data)  # converts to a json structure
    return json_data


def unused_json_farm_invites_view(request):
    context = {
        'body': 'no body to share',
        'header': 'farm invites view',
    }
    return JsonResponse(context)


def unused_page_farm_invites_view(request):
    context = {
        'release': get_version_json(request),
        "title": "Coming Soon",
        "blurb": "This page is a place holder for what's to come soon.",
        "table_data": 'Shake it like it\'s going out of style!',
        "year": datetime.now().year
    }
    return render(request, "farminvite/coming_soon.html", context)


def page_farm_invites_view(request):
    # all_invites = InviteListing.objects.all().order_by('Invite_Date', 'Invite_Secondary')
    this_moment = datetime.now()
    # only events not past, ordered by date, am then pm.. then secondary listings
    all_invites = InviteListing.objects.filter(
        Q(Invite_Date=this_moment.date()) |
        Q(Invite_Date__gt=this_moment.date())).order_by('Invite_Date', 'Invite_Secondary', '-Invite_AM', )

    context = {
        # "roll_list": queryset,
        'release': get_version_json(request),
        "title": "Farm Range Invites",
        "blurb": "Something might have gone wrong.",
        'all_invites': all_invites,
        "year": datetime.now().year
        # "year": all_loads.prod
    }
    return render(request, "farminvite/calendar_list.html", context)


def page_farm_invites_map(request):
    context = {
        'release': get_version_json(request),
        "title": "Farm Invite: Map",
        "table_data": 'Shake it like it\'s going out of style!',
        "year": datetime.now().year
    }
    return render(request, "farminvite/farm_map.html", context)


def page_farm_invites_map_fake(request):
    context = {
        'release': get_version_json(request),
        "title": "Coming Soon",
        "blurb": "This page is a place holder for what's to come soon.",
        "table_data": 'Shake it like it\'s going out of style!',
        "year": datetime.now().year
    }
    return render(request, "farminvite/fake_map.html", context)
