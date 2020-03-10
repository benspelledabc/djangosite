from datetime import datetime
from django.conf import settings
from django.db.models import F, FloatField, ExpressionWrapper, TextField, IntegerField
from django.http import JsonResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
import os
import json
from .models import HandLoad, EstimatedDope, Firearm
from announcements.get_news import get_news, get_version_json

import logging
# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)


def page_foot_pound_calc(request):
    context = {
        'release': get_version_json(),
        "title": "Foot Pound Calculator",
        "blurb": "I moved the calculator to its own page.",
        "copy_year": datetime.now().year,
    }
    return render(request, "loaddata/foot_pound_calc.html", context)


# Create your views here.
def page_loads(request):
    logger.info("This is not getting logged...")

    all_loads = HandLoad.objects.all().order_by('Is_Sheriff_Load', '-prod', '-projectile__Diameter').annotate(
        prod=ExpressionWrapper(F('projectile__WeightGR') * 0.5 / 7000 / 32.127 * F('Velocity') * F('Velocity'), output_field=FloatField()),
        rps=ExpressionWrapper(F('Velocity') * 720 / F('firearm__inches_per_twist') / 60, output_field=IntegerField())
    )

    context = {
        'release': get_version_json(),
        "title": "Load Data",
        "blurb": "Do your own research, don't use this load data. It might be a pipe bomb in your firearm.",
        'all_loads': all_loads,
        "copy_year": datetime.now().year
    }
    return render(request, "loaddata/djangoad.html", context)


def page_estimated_dope(request, load_pk='3'):
    try:
        selected_load = EstimatedDope.objects.get(hand_load=load_pk)
        context = {
            'load_id': load_pk,
            'release': get_version_json(),
            "title": "Estimated Dope",
            "blurb": "I'll move it to a database setup in a bit.",
            'load_details': selected_load,
            "copy_year": datetime.now().year,
        }
    except ObjectDoesNotExist:
        context = {
            'load_id': load_pk,
            'release': get_version_json(),
            "title": "Master Po Load Data",
            "blurb": "No dope for this load.",
            "copy_year": datetime.now().year,
        }

    return render(request, "loaddata/estimated_dope.html", context)


def page_firearm_detail(request, firearm_pk='3'):
    try:
        selected_firearm = Firearm.objects.get(pk=firearm_pk)

        context = {
            'firearm_id': firearm_pk,
            'release': get_version_json(),
            "title": "Firearm Detail",
            "blurb": "Sometimes knowing your tool is more important than using it quickly.",
            'firearm_details': selected_firearm,
            "copy_year": datetime.now().year,
        }
    except ObjectDoesNotExist:
        context = {
            'load_id': firearm_pk,
            'release': get_version_json(),
            "title": "Master Po Load Data",
            "blurb": "Estimated DOPE not found.",
            "copy_year": datetime.now().year,
        }

    return render(request, "loaddata/firearm_details.html", context)


def sample(request):
    data = {
        'Query': 'Complete',
        'Result': 'The query completed but this is not an endpoint with data.'
    }
    return JsonResponse(data)

# /data/django/IMRUnicorn-Django/
