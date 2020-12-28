from imrunicorn.decorators import unauthenticated_user
from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, \
    get_page_blurb_override, get_restart_notice
from groundhog_logbook.functions import all_groundhog_removals, all_groundhog_removals_by_shooter, \
    all_groundhog_hole_locations, groundhog_removal_scoreboard, \
    groundhogs_by_hour_of_day, groundhogs_by_hour_of_day_by_sex, groundhogs_by_sex, groundhogs_count_by_sex, \
    groundhog_removal_scoreboard_annual, groundhogs_by_month

from imrunicorn.decorators import allowed_groups
from imrunicorn.functions import step_hit_count_by_page
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from dateutil import parser
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


class ChartDataByMonth(APIView):
    authentication_classes = []
    permission_classes = []

    # todo: this needs work and fixing...
    def get(self, request, format=None):
        by_month = groundhogs_by_month()
        print("view: {0}".format(by_month))

        labels = []
        default_items = []

        for item in by_month:
            # dt = item['month']
            # print(dt.month)
            # print(item['month'].strftime("%B"))
            labels.append(item['month'].strftime("%B"))
            # labels.append(dt.month)

        for item in by_month:
            default_items.append(item['kills_per_month'])

        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


def page_charts_by_month(request):
    step_hit_count_by_page(request.path)

    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Groundhog Line Charts",
        "blurb": get_page_blurb_override('groundhog_logbook/graphic_charts/'),
    }
    return render(request, "groundhog_logbook/groundhog_graphic_month.html", context)


class ChartDataByTime(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        by_hour = groundhogs_by_hour_of_day()
        labels = []
        default_items = []

        for item in by_hour:
            labels.append(item['hour'])

        for item in by_hour:
            default_items.append(item['kills_per_hour'])

        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


def page_charts_by_time(request):
    step_hit_count_by_page(request.path)

    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Groundhog Line Charts",
        "blurb": get_page_blurb_override('groundhog_logbook/graphic_charts/'),
    }
    return render(request, "groundhog_logbook/groundhog_graphic_time.html", context)


class ChartDataBySex(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        total_count = groundhogs_count_by_sex()
        male_count = groundhogs_count_by_sex("MALE")
        female_count = groundhogs_count_by_sex("FEMALE")
        unknown_count = groundhogs_count_by_sex("UNKNOWN")

        labels = ["Total", "Male", "Female", "Unknown"]
        default_items = [total_count, male_count, female_count, unknown_count]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


def page_charts_by_sex(request):
    step_hit_count_by_page(request.path)

    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Groundhog Line Charts",
        "blurb": get_page_blurb_override('groundhog_logbook/graphic_charts/'),
    }
    return render(request, "groundhog_logbook/groundhog_graphic_sex.html", context)


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


# @unauthenticated_user
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


@allowed_groups(allowed_groupname_list=['groundhog_hole_knowledge'])
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


def page_groundhog_removals_scoreboard_annual(request):
    step_hit_count_by_page(request.path)
    logs = groundhog_removal_scoreboard_annual()

    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        "logs": logs,
        'release': get_version_json(),
        "title": "Top Groundhog Removers",
        "blurb": get_page_blurb_override('groundhog_logbook/removal_scoreboard/'),
    }
    return render(request, "groundhog_logbook/groundhog_removal_scoreboard_annual.html", context)

