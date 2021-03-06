from imrunicorn.decorators import unauthenticated_user
from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, \
    get_page_blurb_override, get_restart_notice
from groundhog_logbook.functions import all_groundhog_removals, all_groundhog_removals_by_shooter, \
    all_groundhog_hole_locations, groundhog_removal_scoreboard, \
    groundhogs_by_hour_of_day, groundhogs_by_hour_of_day_by_sex, groundhogs_by_sex, groundhogs_count_by_sex, \
    groundhog_removal_scoreboard_annual, groundhogs_by_month, groundhogs_by_cloud_level, groundhogs_by_temperature, \
    groundhogs_by_year, groundhogs_by_caliber, groundhogs_by_distance

from imrunicorn.decorators import allowed_groups
from imrunicorn.functions import step_hit_count_by_page, get_weather
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime, timedelta
from dateutil import parser
from django.shortcuts import render
from django.views.generic import View
from rest_framework import viewsets
from django.contrib.humanize.templatetags.humanize import ordinal
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()


def page_charts_by_remover(request):
    step_hit_count_by_page(request.path)

    context = {
        "graph_api_node": '/groundhog_logbook/api/chart/by_remover/data/',
        "graph_header": "# of Groundhog Removals (By Remover)",
        "graph_message": "This is a total number of removals since we started tracking them.",
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Groundhog Line Charts",
        "blurb": get_page_blurb_override('groundhog_logbook/graphic_charts/'),
    }
    return render(request, "groundhog_logbook/groundhog_graphic_generic.html", context)


class ChartDataByRemover(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        by_hour = groundhog_removal_scoreboard()
        labels = []
        default_items = []

        for item in by_hour:
            shooter_name = ""
            if item['shooter__userprofile__preferred_display_name']:
                shooter_name = item['shooter__userprofile__preferred_display_name']
            else:
                shooter_name = item['shooter__username']
            labels.append(shooter_name)

        for item in by_hour:
            default_items.append(item['removals'])

        data = {
            "labels": labels,
            "default": default_items,
            "endpoint": "/groundhog_logbook/api/chart/by_remover/data/",
            "graph_title": "# of Groundhog Removals (By Remover)"
        }
        return Response(data)


def page_charts_by_temperature(request):
    step_hit_count_by_page(request.path)

    context = {
        "graph_api_node": '/groundhog_logbook/api/chart/by_temperature/data/',
        "graph_header": "# of Groundhog Removals (By Temperature)",
        "graph_message": "Temps are rounded to nearest 5 degrees.",
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Groundhog Line Charts",
        "blurb": get_page_blurb_override('groundhog_logbook/graphic_charts/'),
    }
    return render(request, "groundhog_logbook/groundhog_graphic_generic.html", context)


class ChartDataByTemperature(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        by_hour = groundhogs_by_temperature()
        labels = []
        default_items = []

        for item in by_hour:
            labels.append(item['estimated_temperature'])

        for item in by_hour:
            default_items.append(item['kills'])

        data = {
            "labels": labels,
            "default": default_items,
            "endpoint": "/groundhog_logbook/api/chart/by_temperature/data/",
            "graph_title": "# of Groundhog Removals (By Temperature)"
        }
        return Response(data)


class ChartDataByCloudLevel(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        clear_sky = groundhogs_by_cloud_level("Clear Sky")
        few_clouds = groundhogs_by_cloud_level("Few Clouds")
        scattered_clouds = groundhogs_by_cloud_level("Scattered Clouds")

        broken_clouds = groundhogs_by_cloud_level("Broken Clouds")
        shower_rain = groundhogs_by_cloud_level("Shower/Rain")
        rain = groundhogs_by_cloud_level("Rain")

        thunderstorm = groundhogs_by_cloud_level("Thunderstorm")
        snow = groundhogs_by_cloud_level("Snow")
        mist = groundhogs_by_cloud_level("Mist")

        unknown_count = groundhogs_by_cloud_level("Unknown")

        labels = ["Clear Sky", "Few Clouds", "Scattered Clouds",
                  "Broken Clouds", "Shower/Rain", "Rain", "Thunderstorm",
                  "Snow", "Mist", "Unknown"]
        default_items = [clear_sky, few_clouds, scattered_clouds, broken_clouds,
                         shower_rain, rain, thunderstorm, snow, mist, unknown_count]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


def page_charts_by_cloud_level(request):
    step_hit_count_by_page(request.path)

    context = {
        "graph_api_node": '/groundhog_logbook/api/chart/by_cloud_level/data/',
        "graph_header": "# of Groundhog Removals (By Cloud Level)",
        "graph_message": "We didn't start tracking the cloud level until 2021. Data before that will be listed as "
                         "'Unknown' unless we find a site that shows historical data for clouds at the time of day in "
                         "question.",
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Groundhog Line Charts",
        "blurb": get_page_blurb_override('groundhog_logbook/graphic_charts/'),
    }
    return render(request, "groundhog_logbook/groundhog_graphic_generic.html", context)


class ChartDataByMonth(APIView):
    authentication_classes = []
    permission_classes = []

    # todo: this needs work and fixing...
    def get(self, request, format=None):
        by_month = groundhogs_by_month()

        labels = []
        default_items = []

        for item in by_month:
            labels.append(item['month'].strftime("%B"))

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
        "graph_api_node": '/groundhog_logbook/api/chart/by_month/data/',
        "graph_header": "# of Groundhog Removals (By Month)",
        "graph_message": "",
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Groundhog Line Charts",
        "blurb": get_page_blurb_override('groundhog_logbook/graphic_charts/'),
    }
    return render(request, "groundhog_logbook/groundhog_graphic_generic.html", context)


class ChartDataByYear(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        by_year = groundhogs_by_year()
        print("view: {0}".format(by_year))

        labels = []
        default_items = []

        for item in by_year:
            labels.append(item['year'].strftime("%Y"))

        for item in by_year:
            default_items.append(item['kills_per_year'])

        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


def page_charts_by_year(request):
    step_hit_count_by_page(request.path)

    context = {
        "graph_api_node": '/groundhog_logbook/api/chart/by_year/data/',
        "graph_header": "# of Groundhog Removals (By Year)",
        "graph_message": "",
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Groundhog Line Charts",
        "blurb": get_page_blurb_override('groundhog_logbook/graphic_charts/'),
    }
    return render(request, "groundhog_logbook/groundhog_graphic_generic.html", context)


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
        "graph_api_node": '/groundhog_logbook/api/chart/by_time/data/',
        "graph_header": "# of Groundhog Removals (By Time)",
        "graph_message": "We're only showing by the removals by the hour.",
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Groundhog Line Charts",
        "blurb": get_page_blurb_override('groundhog_logbook/graphic_charts/'),
    }
    return render(request, "groundhog_logbook/groundhog_graphic_generic.html", context)


class ChartDataBySex(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        total_count = groundhogs_count_by_sex()
        male_count = groundhogs_count_by_sex("MALE")
        female_count = groundhogs_count_by_sex("FEMALE")
        unknown_count = groundhogs_count_by_sex("UNKNOWN")

        labels = ["Male", "Female", "Unknown"]
        default_items = [male_count, female_count, unknown_count]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


def page_charts_by_sex(request):
    step_hit_count_by_page(request.path)

    context = {
        "graph_api_node": '/groundhog_logbook/api/chart/by_sex/data/',
        "graph_header": "# of Groundhog Removals (By Sex)",
        "graph_message": "Sometimes we don't check the sex because of heat or some other reason. Sometimes the "
                         "sexy bits are blow off, these are marked as 'unknown'.",
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Groundhog Line Charts",
        "blurb": get_page_blurb_override('groundhog_logbook/graphic_charts/'),
    }
    return render(request, "groundhog_logbook/groundhog_graphic_generic.html", context)


# Create your views here.
# https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html

def page_charts(request):
    step_hit_count_by_page(request.path)
    logs = groundhogs_by_hour_of_day()
    logs_sexy = groundhogs_by_sex()
    logs_sexy_hour = groundhogs_by_hour_of_day_by_sex()
    context = {
        # "restart": get_restart_notice,
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
    all_news = all_groundhog_removals(request)
    weather = get_weather(request)
    context = {
        "weather": weather,
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        "all_news": all_news,
        'release': get_version_json(),
        "title": "Groundhog Logbook",
        # "blurb": "this is a blurb that goes on the page for testing. blah blah blah.",
        "blurb": get_page_blurb_override('groundhog_logbook/by_shooter/'),
    }

    # print(weather)
    return render(request, "groundhog_logbook/all_groundhog_kills.html", context)


@allowed_groups(allowed_groupname_list=['groundhog_hole_knowledge'])
def page_all_groundhog_locations(request):
    step_hit_count_by_page(request.path)
    context = {
        # "restart": get_restart_notice,
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
        # "restart": get_restart_notice,
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
        # "restart": get_restart_notice,
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
    last_year = datetime.now() - timedelta(days=(1*365))
    last_year_year = last_year.strftime("%Y")
    last_year_month = last_year.strftime("%B")
    last_year_day = last_year.strftime("%m")
    rolling_year_date = "{0} {1} of {2}".format(last_year_month, ordinal(last_year_day), last_year_year)

    now = datetime.now()
    now_year = now.strftime("%Y")
    now_month = now.strftime("%B")
    now_day = now.strftime("%m")
    now_string = "{0} {1} of {2}".format(now_month, ordinal(now_day), now_year)

    context = {
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        "rolling_year_date": rolling_year_date,
        "datetime_now": now_string,
        "logs": logs,
        'release': get_version_json(),
        "title": "Top Groundhog Removers",
        "blurb": get_page_blurb_override('groundhog_logbook/removal_scoreboard/'),
    }
    return render(request, "groundhog_logbook/groundhog_removal_scoreboard_annual.html", context)


class ChartDataByCaliber(APIView):
    authentication_classes = []
    permission_classes = []

    # todo: this needs work and fixing...
    def get(self, request, format=None):
        by_month = groundhogs_by_caliber()

        labels = []
        default_items = []

        for item in by_month:
            labels.append(item['firearm__caliber__name'])

        for item in by_month:
            default_items.append(item['removals'])

        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


def page_charts_by_caliber(request):
    step_hit_count_by_page(request.path)

    context = {
        "graph_api_node": '/groundhog_logbook/api/chart/by_caliber/data/',
        "graph_header": "# of Groundhog Removals (By Caliber)",
        "graph_message": "",
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Groundhog Line Charts",
        "blurb": get_page_blurb_override('groundhog_logbook/graphic_charts/'),
    }
    return render(request, "groundhog_logbook/groundhog_graphic_generic.html", context)


class ChartDataByDistance(APIView):
    authentication_classes = []
    permission_classes = []

    # todo: this needs work and fixing...
    def get(self, request, format=None):
        by_month = groundhogs_by_distance()

        labels = []
        default_items = []

        for item in by_month:
            labels.append(item['shot_distance_yards'])

        for item in by_month:
            default_items.append(item['kills'])

        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


def page_charts_by_distance(request):
    step_hit_count_by_page(request.path)

    context = {
        "graph_api_node": '/groundhog_logbook/api/chart/by_distance/data/',
        "graph_header": "# of Groundhog Removals (By Distance)",
        "graph_message": "Rounded in 25 yard increments if under 400 yards.",
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Groundhog Line Charts",
        "blurb": get_page_blurb_override('groundhog_logbook/graphic_charts/'),
    }
    return render(request, "groundhog_logbook/groundhog_graphic_generic.html", context)
