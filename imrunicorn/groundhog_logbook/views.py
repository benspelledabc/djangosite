from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, get_page_blurb_override
from groundhog_logbook.functions import all_groundhog_removals, all_groundhog_removals_by_shooter, all_groundhog_hole_locations
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets


# Create your views here.
def page_all_groundhog_removals(request):
    all_news = all_groundhog_removals

    context = {
        "copy_year": datetime.now().year,
        "all_news": all_news,
        'release': get_version_json(),
        "title": "Groundhog Logbook",
        "blurb": get_page_blurb_override('groundhog_logbook/by_shooter/'),
    }
    return render(request, "groundhog_logbook/all_groundhog_kills.html", context)


def page_all_groundhog_locations(request):
    context = {
        "copy_year": datetime.now().year,
        "list_of_holes": all_groundhog_hole_locations(),
        'release': get_version_json(),
        "title": "Groundhog Hole Locations",
        "blurb": get_page_blurb_override('groundhog_logbook/locations/'),
    }
    return render(request, "groundhog_logbook/all_groundhog_hole_locations.html", context)


def page_all_groundhog_removals_by_shooter_pk(request, shooter_pk=1):
    all_news = all_groundhog_removals_by_shooter(shooter_pk)

    context = {
        "copy_year": datetime.now().year,
        "all_news": all_news,
        'release': get_version_json(),
        "title": "Groundhog Logbook",
        "blurb": get_page_blurb_override('groundhog_logbook/by_shooter/'),
    }
    return render(request, "groundhog_logbook/all_groundhog_kills.html", context)
