from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, get_page_blurb_override
from groundhog_logbook.functions import all_groundhog_removals, all_groundhog_removals_by_shooter, all_groundhog_hole_locations, groundhog_removal_scoreboard
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets


# Create your views here.
# https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html

def page_charts(request):
    context = {
        "copy_year": datetime.now().year,
        "all_news": "disabled",
        'release': get_version_json(),
        "title": "Groundhog Charts",
        "blurb": get_page_blurb_override('groundhog_logbook/charts/'),
    }
    # <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    # etc etc
    # https://plotly.com/javascript/bar-charts/#
    # https://plotly.com/javascript/getting-started/

    return render(request, "groundhog_logbook/groundhog_charts.html", context)


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


def page_groundhog_removals_scoreboard(request):
    logs = groundhog_removal_scoreboard()

    context = {
        "copy_year": datetime.now().year,
        "logs": logs,
        'release': get_version_json(),
        "title": "Top Groundhog Removers",
        "blurb": get_page_blurb_override('groundhog_logbook/removal_scoreboard/'),
    }
    return render(request, "groundhog_logbook/groundhog_removal_scoreboard.html", context)
