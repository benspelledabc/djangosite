from datetime import datetime
from django.conf import settings
from django.db.models import F, FloatField, ExpressionWrapper
from django.http import JsonResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
import os
import json
from .models import HandLoad, EstimatedDope
from announcements.get_news import get_news, get_version_json


# Create your views here.
def page_loads(request):
    all_loads = HandLoad.objects.all().order_by('Is_Sheriff_Load', '-prod', '-projectile__Diameter').annotate(
        prod=ExpressionWrapper(F('projectile__WeightGR') * 0.5 / 7000 / 32.127 * F('Velocity') * F('Velocity'),
                               output_field=FloatField()))

    context = {
        # "roll_list": queryset,
        'release': get_version_json(),
        "title": "Master Po: Load Data",
        "blurb": "I'll move it to a database setup in a bit.",
        # changed this from tabledata
        "table_data": 'This should be from the database... jackle.',
        'all_loads': all_loads,
        "year": datetime.now().year
        # "year": all_loads.prod
    }
    return render(request, "loaddata/djangoad.html", context)


def page_estimated_dope(request, load_pk='3'):
    # all_loads = HandLoad.objects.all().order_by('Is_Sheriff_Load', '-prod', '-projectile__Diameter').annotate(
    #     prod=ExpressionWrapper(F('projectile__WeightGR') * 0.5 / 7000 / 32.127 * F('Velocity') * F('Velocity'),
    #                            output_field=FloatField()))

    # selected_load = EstimatedDope.objects.get(hand_load=load_pk)

    try:
        selected_load = EstimatedDope.objects.get(hand_load=load_pk)
        context = {
            'load_id': load_pk,
            # "roll_list": queryset,
            'release': get_version_json(),
            "title": "Master Po Load Data",
            "blurb": "I'll move it to a database setup in a bit.",
            'load_details': selected_load,
            "year": datetime.now().year,
        }
    except ObjectDoesNotExist:
        context = {
            'load_id': load_pk,
            # "roll_list": queryset,
            'release': get_version_json(),
            "title": "Master Po Load Data",
            "blurb": "Estimated DOPE not found.",
            # 'load_details': 'selected_load',
            "year": datetime.now().year,
        }

    return render(request, "loaddata/estimated_dope.html", context)


def page_avg_and_sd_calc(request):
    context = {
        # "roll_list": queryset,
        'release': get_version_json(),
        "title": "Avg & SD Calc",
        "blurb": "This page is a place holder for what's to come soon.",
        "table_data": 'Lorem ipsum Django info is from '
                      '<a href="https://google.com" target="_blank">here</a>.',
        "year": datetime.now().year
    }
    return render(request, "loaddata/avg_and_sd_calc.html", context)


def sample(request):
    data = {
        'Query': 'Complete',
        'Result': 'The query completed but this is not an endpoint with data.'
    }
    return JsonResponse(data)
