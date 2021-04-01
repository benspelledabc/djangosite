from django.shortcuts import render
import calendar
from rest_framework.views import APIView
from rest_framework.response import Response
from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, \
    get_page_blurb_override, get_restart_notice
from imrunicorn.functions import step_hit_count_by_page
from .functions import requests_by_year, requests_by_month
from datetime import datetime
from django.shortcuts import render


def page_blank(request):
    step_hit_count_by_page(request.path)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "DCSA Info: Blank",
        "blurb": get_page_blurb_override('dcsa_info/blank/'),
    }
    return render(request, "dcsa_info/blank.html", context)


def page_success_example(request):
    step_hit_count_by_page(request.path)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "DCSA Info: Success Examples",
        "blurb": get_page_blurb_override('dcsa_info/success_example/'),
    }
    return render(request, "dcsa_info/success_examples.html", context)


def page_info(request):
    step_hit_count_by_page(request.path)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "DCSA Info",
        "blurb": get_page_blurb_override('dcsa_info/info/'),
    }
    return render(request, "dcsa_info/info.html", context)


def page_coming_soon(request):
    step_hit_count_by_page(request.path)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "DCSA Info: Coming Soon",
        "blurb": get_page_blurb_override('dcsa_info/coming_soon/'),
    }
    return render(request, "dcsa_info/coming_soon.html", context)


# ############ Graphic Charts
class ChartDataByYear(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        by_year = requests_by_year()
        print("view: {0}".format(by_year))

        labels = []
        default_items = []

        for item in by_year:
            labels.append(item['year'].strftime("%Y"))

        for item in by_year:
            default_items.append(item['requests_per_year'])

        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


def page_charts_by_year(request):
    step_hit_count_by_page(request.path)

    context = {
        "graph_api_node": '/dcsa_info/api/chart/by_year/data/',
        "graph_header": "# of Requests (By Year)",
        "graph_message": "",
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "DCSA Info: Charts (Year)",
        "blurb": get_page_blurb_override('dcsa_info/graphic_charts/'),
    }
    return render(request, "dcsa_info/dcsa_graphic_generic.html", context)


class ChartDataByMonth(APIView):
    authentication_classes = []
    permission_classes = []

    # todo: this needs work and fixing...
    def get(self, request, format=None):
        by_month = requests_by_month()

        labels = []
        default_items = []

        for item in by_month:
            month_number = item['month']
            labels.append(calendar.month_name[month_number])

        for item in by_month:
            default_items.append(item['requests_per_month'])

        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


def page_charts_by_month(request):
    step_hit_count_by_page(request.path)

    context = {
        "graph_api_node": '/dcsa_info/api/chart/by_month/data/',
        "graph_header": "# of Requests (By Month)",
        "graph_message": "",
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "DCSA Info: Charts (Month)",
        "blurb": get_page_blurb_override('dcsa_info/graphic_charts/'),
    }
    return render(request, "dcsa_info/dcsa_graphic_generic.html", context)
