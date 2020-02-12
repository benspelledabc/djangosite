from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from announcements.get_news import get_news, get_version_json


def page_six_steps_of_firing_a_shot(request):
    # http://appleseedshoot.blogspot.com/2008/03/six-steps-of-firing-shot.html
    context = {
        "show_lorem": False,
        'release': get_version_json(),
        "title": "6 steps of firing a shot",
        "blurb": "This page is a place holder for what's to come soon.",
        "table_data": '',
        "year": datetime.now().year
    }
    return render(request, "shooting_logbook/six_steps_to_firing_a_shot.html", context)


def page_reading_wind_mirage(request):
    context = {
        'release': get_version_json(),
        "title": "Reading Wind Mirage",
        "blurb": "This page is a place holder for what's to come soon.",
        "year": datetime.now().year
    }
    return render(request, "shooting_logbook/reading_wind_mirage.html", context)


def sample(request):
    data = {
        'Query': 'Complete',
        'Result': 'The query completed but this is not an endpoint with data.'
    }
    return JsonResponse(data)
