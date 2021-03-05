from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, \
    get_page_blurb_override, get_restart_notice
from imrunicorn.functions import step_hit_count_by_page
from deer_harvest_logbook.functions import all_harvests, all_harvests_by_shooter
from deer_harvest_logbook.functions import harvests_by_hour_of_day, harvests_by_score, harvests_by_sex, \
    harvests_by_month, harvests_by_year, harvests_scoreboard, harvests_by_temperature, harvests_by_cloud_level
from datetime import datetime
from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


User = get_user_model()


# def page_charts(request):
#     step_hit_count_by_page(request.path)
#     logs = harvests_by_hour_of_day()
#     logs_sexy = harvests_by_sex()
#     logs_by_score = harvests_by_score()
#     context = {
#         # "restart": get_restart_notice,
#         "copy_year": datetime.now().year,
#         "logs": logs,
#         "logs_sexy": logs_sexy,
#         "logs_sexy_hour": logs_by_score,
#         'release': get_version_json(),
#         "title": "Harvest Charts",
#         "blurb": get_page_blurb_override('deer_harvest_logbook/charts/'),
#     }
#     return render(request, "deer_harvest_logbook/harvest_charts.html", context)


def page_charts(request):
    step_hit_count_by_page(request.path)
    logs = harvests_by_hour_of_day()
    logs_sexy = harvests_by_sex()
    logs_by_score = harvests_by_score()
    context = {
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        "logs": logs,
        "logs_sexy": logs_sexy,
        "logs_sexy_hour": logs_by_score,
        'release': get_version_json(),
        "title": "Harvest Charts",
        "blurb": get_page_blurb_override('deer_harvest_logbook/charts/'),
    }
    return render(request, "deer_harvest_logbook/harvest_charts.html", context)


def page_point_system(request):
    step_hit_count_by_page(request.path)
    context = {
        "hide_points": True,
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Deer Harvest Point System",
        "blurb": get_page_blurb_override('deer_harvest_logbook/point_system/'),
    }
    return render(request, "deer_harvest_logbook/point_system.html", context)


def page_point_system_show_points(request):
    step_hit_count_by_page(request.path)
    context = {
        "hide_points": False,
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Deer Harvest Point System",
        "blurb": get_page_blurb_override('deer_harvest_logbook/point_system/'),
    }
    return render(request, "deer_harvest_logbook/point_system.html", context)


def page_all_harvests(request):
    step_hit_count_by_page(request.path)
    context = {
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        "all_news": all_harvests(request),
        'release': get_version_json(),
        "title": "Deer Harvest Logbook",
        "blurb": get_page_blurb_override('deer_harvest_logbook/'),
    }
    return render(request, "deer_harvest_logbook/all_harvests.html", context)


def page_all_harvests_by_shooter_pk(request, shooter_pk=1):
    step_hit_count_by_page(request.path)
    # all_news = all_groundhog_removals_by_shooter(shooter_pk)
    all_news = all_harvests
    context = {
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        "all_news": all_news,
        'release': get_version_json(),
        "title": "Deer Harvest Logbook",
        "blurb": get_page_blurb_override('deer_harvest_logbook/by_shooter/'),
    }
    return render(request, "deer_harvest_logbook/all_harvests.html", context)


# ############ CHARTS #############
class ChartDataByTime(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        by_hour = harvests_by_hour_of_day()
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
        "graph_api_node": '/deer_harvest_logbook/api/chart/by_time/data/',
        "graph_header": "# of Deer Removals (By Time)",
        "graph_message": "We're only showing by the removals by the hour.",
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Deer Line Charts",
        "blurb": get_page_blurb_override('deer_harvest_logbook/graphic_charts/'),
    }
    return render(request, "deer_harvest_logbook/deer_graphic_generic.html", context)


class ChartDataBySex(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        total_count = harvests_by_sex()
        male_count = harvests_by_sex("MALE")
        female_count = harvests_by_sex("FEMALE")
        unknown_count = harvests_by_sex("UNKNOWN")

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
        "graph_api_node": '/deer_harvest_logbook/api/chart/by_sex/data/',
        "graph_header": "# of Deer Removals (By Sex)",
        "graph_message": "If the sex is listed as unknown, it's because the log is wrong.",
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Deer Line Charts",
        "blurb": get_page_blurb_override('deer_harvest_logbook/graphic_charts/'),
    }
    return render(request, "deer_harvest_logbook/deer_graphic_generic.html", context)


class ChartDataByMonth(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        by_month = harvests_by_month()
        print("view: {0}".format(by_month))

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
        "graph_api_node": '/deer_harvest_logbook/api/chart/by_month/data/',
        "graph_header": "# of Deer Removals (By Month)",
        "graph_message": "",
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Deer Line Charts",
        "blurb": get_page_blurb_override('deer_harvest_logbook/graphic_charts/'),
    }
    return render(request, "deer_harvest_logbook/deer_graphic_generic.html", context)


class ChartDataByYear(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        by_year = harvests_by_year()
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
        "graph_api_node": '/deer_harvest_logbook/api/chart/by_year/data/',
        "graph_header": "# of Deer Removals (By Year)",
        "graph_message": "",
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Deer Line Charts",
        "blurb": get_page_blurb_override('deer_harvest_logbook/graphic_charts/'),
    }
    return render(request, "deer_harvest_logbook/deer_graphic_generic.html", context)


def page_charts_by_remover(request):
    step_hit_count_by_page(request.path)
    context = {
        "graph_api_node": '/deer_harvest_logbook/api/chart/by_remover/data/',
        "graph_header": "# of Deer Removals (By Remover)",
        "graph_message": "This is a total number of removals since we started tracking them.",
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Deer Line Charts",
        "blurb": get_page_blurb_override('deer_harvest_logbook/graphic_charts/'),
    }
    return render(request, "deer_harvest_logbook/deer_graphic_generic.html", context)


class ChartDataByRemover(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        by_hour = harvests_scoreboard()
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
            "endpoint": "/deer_harvest_logbook/api/chart/by_remover/data/",
            "graph_title": "# of Deer Removals (By Remover)"
        }
        return Response(data)


def page_charts_by_temperature(request):
    step_hit_count_by_page(request.path)

    context = {
        "graph_api_node": '/deer_harvest_logbook/api/chart/by_temperature/data/',
        "graph_header": "# of Deer Removals (By Temperature)",
        "graph_message": "Temps are rounded to nearest 5 degrees.",
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Deer Line Charts",
        "blurb": get_page_blurb_override('deer_harvest_logbook/graphic_charts/'),
    }
    return render(request, "deer_harvest_logbook/deer_graphic_generic.html", context)


class ChartDataByTemperature(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        by_hour = harvests_by_temperature()
        labels = []
        default_items = []

        for item in by_hour:
            labels.append(item['estimated_temperature'])

        for item in by_hour:
            default_items.append(item['kills'])

        data = {
            "labels": labels,
            "default": default_items,
            "endpoint": "/deer_harvest_logbook/api/chart/by_temperature/data/",
            "graph_title": "# of Deer Removals (By Temperature)"
        }
        return Response(data)


class ChartDataByCloudLevel(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        clear_sky = harvests_by_cloud_level("Clear Sky")
        few_clouds = harvests_by_cloud_level("Few Clouds")
        scattered_clouds = harvests_by_cloud_level("Scattered Clouds")

        broken_clouds = harvests_by_cloud_level("Broken Clouds")
        shower_rain = harvests_by_cloud_level("Shower/Rain")
        rain = harvests_by_cloud_level("Rain")

        thunderstorm = harvests_by_cloud_level("Thunderstorm")
        snow = harvests_by_cloud_level("Snow")
        mist = harvests_by_cloud_level("Mist")

        unknown_count = harvests_by_cloud_level("Unknown")

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
        "graph_api_node": '/deer_harvest_logbook/api/chart/by_cloud_level/data/',
        "graph_header": "# of Deer Removals (By Cloud Level)",
        "graph_message": "We didn't start tracking the cloud level until 2021. Data before that will be listed as "
                         "'Unknown' unless we find a site that shows historical data for clouds at the time of day in "
                         "question.",
        # "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Deer Line Charts",
        "blurb": get_page_blurb_override('deer_harvest_logbook/graphic_charts/'),
    }
    return render(request, "deer_harvest_logbook/deer_graphic_generic.html", context)

