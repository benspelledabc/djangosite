from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, \
    get_page_blurb_override, get_restart_notice
from groundhog_logbook.functions import all_groundhog_removals, all_groundhog_removals_by_shooter
from groundhog_logbook.functions import all_groundhog_hole_locations, groundhog_removal_scoreboard
from groundhog_logbook.functions import groundhogs_by_hour_of_day, groundhogs_by_hour_of_day_by_sex, groundhogs_by_sex
from imrunicorn.functions import step_hit_count_by_page
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.views.generic import View
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            "restart": get_restart_notice,
            "groundhog_chart_data": groundhogs_by_hour_of_day(),
            "website_user_count": User.objects.all().count(),
            "extra_info": "I'm moving the data to a reusable format. Please excuse my fun...",
        }
        return Response(data)


# Create your views here.
# https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html

def page_charts(request):
    step_hit_count_by_page(request.path)
    logs = groundhogs_by_hour_of_day()
    logs_sexy = groundhogs_by_sex()
    logs_sexy_hour = groundhogs_by_hour_of_day_by_sex()
    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        "logs": logs,
        "logs_sexy": logs_sexy,
        "logs_sexy_hour": logs_sexy_hour,
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
    step_hit_count_by_page(request.path)
    all_news = all_groundhog_removals

    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        "all_news": all_news,
        'release': get_version_json(),
        "title": "Groundhog Logbook",
        "blurb": get_page_blurb_override('groundhog_logbook/by_shooter/'),
    }
    return render(request, "groundhog_logbook/all_groundhog_kills.html", context)


def page_all_groundhog_locations(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        "list_of_holes": all_groundhog_hole_locations(),
        'release': get_version_json(),
        "title": "Groundhog Hole Locations",
        "blurb": get_page_blurb_override('groundhog_logbook/locations/'),
    }
    return render(request, "groundhog_logbook/all_groundhog_hole_locations.html", context)


def page_all_groundhog_removals_by_shooter_pk(request, shooter_pk=1):
    step_hit_count_by_page(request.path)
    all_news = all_groundhog_removals_by_shooter(shooter_pk)

    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        "all_news": all_news,
        'release': get_version_json(),
        "title": "Groundhog Logbook",
        "blurb": get_page_blurb_override('groundhog_logbook/by_shooter/'),
    }
    return render(request, "groundhog_logbook/all_groundhog_kills.html", context)


def page_groundhog_removals_scoreboard(request):
    step_hit_count_by_page(request.path)
    logs = groundhog_removal_scoreboard()

    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        "logs": logs,
        'release': get_version_json(),
        "title": "Top Groundhog Removers",
        "blurb": get_page_blurb_override('groundhog_logbook/removal_scoreboard/'),
    }
    return render(request, "groundhog_logbook/groundhog_removal_scoreboard.html", context)
