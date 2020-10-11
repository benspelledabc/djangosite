from datetime import datetime
from django.conf import settings
from django.db.models import F, FloatField, ExpressionWrapper, TextField, IntegerField
from django.http import JsonResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
import os
import json

from .models import HandLoad, EstimatedDope, Firearm, Caliber, Powder, Projectile
from announcements.get_news import get_news, get_version_json, get_page_blurb_override, get_restart_notice
from imrunicorn.decorators import unauthenticated_user, allowed_groups
from .forms import CaliberForm, PowderForm, ProjectileForm

import logging
# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)


def firearm_create_view(request):
    data = {"restart": get_restart_notice,'Query': 'Complete',
            'Result': 'The query completed but this is not an endpoint with data.'}
    return JsonResponse(data)


def docker_update_test(request):
    data = {"restart": get_restart_notice, 'Query': 'Complete',
            'Result': 'The query loaded and stuff sooo it might be good.'}
    return JsonResponse(data)


def projectile_create_view(request):
    # data = {'Query': 'Complete', 'Result': 'The query completed but this is not an endpoint with data.'}
    # return JsonResponse(data)
    form = ProjectileForm(request.POST or None)
    if form.is_valid():
        # over ride values to track the submission
        safe_form = form.save(commit=False)
        safe_form.author_pk = request.user.pk
        safe_form.is_approved = False
        safe_form.save()

        form = ProjectileForm()

    all_records = Projectile.objects.all().order_by('WeightGR', '-Manufacture', '-Name')

    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Projectile Creation Tool",
        "blurb": get_page_blurb_override('load_data/toolbox/create_projectile/'),
        "copy_year": datetime.now().year,
        "all_projectiles": all_records,
        'form': form,
    }
    return render(request, "loaddata/projectile_create.html", context)


def powder_create_view(request):
    # data = {'Query': 'Complete', 'Result': 'The query completed but this is not an endpoint with data.'}
    # return JsonResponse(data)
    form = PowderForm(request.POST or None)
    if form.is_valid():
        # over ride values to track the submission
        safe_form = form.save(commit=False)
        safe_form.author_pk = request.user.pk
        safe_form.is_approved = False
        safe_form.save()

        form = PowderForm()

    all_powders = Powder.objects.all().order_by('-name')

    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Powder Creation Tool",
        # "blurb": "I moved the calculator to its own page.",
        "blurb": get_page_blurb_override('load_data/toolbox/create_powder/'),
        "copy_year": datetime.now().year,
        "all_powders": all_powders,
        'form': form,
    }
    return render(request, "loaddata/powder_create.html", context)


def caliber_create_view(request):
    form = CaliberForm(request.POST or None)
    if form.is_valid():
        # over ride values to track the submission
        safe_form = form.save(commit=False)
        safe_form.author_pk = request.user.pk
        safe_form.is_approved = False
        safe_form.save()

        form = CaliberForm()

    all_calibers = Caliber.objects.all().order_by('-diameter')

    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Caliber Creation Tool",
        # "blurb": "I moved the calculator to its own page.",
        "blurb": get_page_blurb_override('load_data/toolbox/create_caliber/'),
        "copy_year": datetime.now().year,
        "all_calibers": all_calibers,
        'form': form,
    }
    return render(request, "loaddata/caliber_create.html", context)


def caliber_create_view_lkg(request):
    form = CaliberForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CaliberForm()

    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Caliber Creation Tool",
        # "blurb": "I moved the calculator to its own page.",
        "blurb": get_page_blurb_override('load_data/toolbox/create_caliber/'),
        "copy_year": datetime.now().year,
        'form': form,
    }
    return render(request, "loaddata/caliber_create.html", context)


def page_foot_pound_calc(request):
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Foot Pound Calculator",
        # "blurb": "I moved the calculator to its own page.",
        "blurb": get_page_blurb_override('load_data/foot_pound_calculator/'),
        "copy_year": datetime.now().year,
    }
    return render(request, "loaddata/foot_pound_calc.html", context)


# Create your views here.
def page_loads_by_type(request, load_type='All'):
    load_type = load_type.lower()
    if load_type == 'ocw':
        load_type = 'ocw'
        all_loads = HandLoad.objects.all().filter(Q(Is_Sheriff_Load=False) | Q(Is_Sheriff_Load=False)).order_by(
            'Is_Sheriff_Load', '-prod', '-projectile__Diameter').annotate(
            prod=ExpressionWrapper(F('projectile__WeightGR') * 0.5 / 7000 / 32.127 * F('Velocity') * F('Velocity'),
                                   output_field=FloatField()),
            rps=ExpressionWrapper(F('Velocity') * 720 / F('firearm__inches_per_twist') / 60,
                                  output_field=IntegerField())
        )
    elif load_type == 'sheriff':
        load_type = 'sheriff'
        all_loads = HandLoad.objects.all().filter(Q(Is_Sheriff_Load=True) | Q(Is_Sheriff_Load=True)).order_by(
            'Is_Sheriff_Load', '-prod', '-projectile__Diameter').annotate(
            prod=ExpressionWrapper(F('projectile__WeightGR') * 0.5 / 7000 / 32.127 * F('Velocity') * F('Velocity'),
                                   output_field=FloatField()),
            rps=ExpressionWrapper(F('Velocity') * 720 / F('firearm__inches_per_twist') / 60,
                                  output_field=IntegerField())
        )
    else:
        load_type = 'all'
        all_loads = HandLoad.objects.all().filter(Q(Is_Sheriff_Load=True) | Q(Is_Sheriff_Load=False)).order_by(
            'Is_Sheriff_Load', '-prod', '-projectile__Diameter').annotate(
            prod=ExpressionWrapper(F('projectile__WeightGR') * 0.5 / 7000 / 32.127 * F('Velocity') * F('Velocity'),
                                   output_field=FloatField()),
            rps=ExpressionWrapper(F('Velocity') * 720 / F('firearm__inches_per_twist') / 60,
                                  output_field=IntegerField())
        )

    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Load Data: %s" % load_type,
        "blurb": get_page_blurb_override('load_data/loads/'),
        'all_loads': all_loads,
        "copy_year": datetime.now().year
    }
    return render(request, "loaddata/djangoad.html", context)


# @allowed_groups(allowed_groupname_list=['content_collection_restricted'])
def page_loads(request):
    logger.info("This is not getting logged...")

    all_loads = HandLoad.objects.all().order_by('Is_Sheriff_Load', '-prod', '-projectile__Diameter').annotate(
        prod=ExpressionWrapper(F('projectile__WeightGR') * 0.5 / 7000 / 32.127 * F('Velocity') * F('Velocity'), output_field=FloatField()),
        rps=ExpressionWrapper(F('Velocity') * 720 / F('firearm__inches_per_twist') / 60, output_field=IntegerField())
    )

    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Load Data",
        # "blurb": "Do your own research, don't use this load data. It might be a pipe bomb in your firearm.",
        "blurb": get_page_blurb_override('load_data/loads/'),
        'all_loads': all_loads,
        "copy_year": datetime.now().year
    }
    return render(request, "loaddata/djangoad.html", context)


# Create your views here.
def page_loads_details(request, load_pk=None):
    context = {
        "restart": get_restart_notice,
        'load_id': load_pk,
        'release': get_version_json(),
        "title": "Can't get detail without an id.",
        # todo: figure out this blurb link.
        # "blurb": get_page_blurb_override('load_data/load_detail/NOT-FOUND'),
        "copy_year": datetime.now().year,
    }

    if load_pk is None:
        return render(request, "loaddata/load_details.html", context)

        # selected_firearm = Firearm.objects.get(pk=firearm_pk)
        # all_loads = HandLoad.objects.all().order_by('Is_Sheriff_Load', '-prod', '-projectile__Diameter').annotate(
        #     prod=ExpressionWrapper(F('projectile__WeightGR') * 0.5 / 7000 / 32.127 * F('Velocity') * F('Velocity'),
        #                            output_field=FloatField()),
        #     rps=ExpressionWrapper(F('Velocity') * 720 / F('firearm__inches_per_twist') / 60,
        #                           output_field=IntegerField())
        # )

    try:
        selected_hand_load = HandLoad.objects.get(pk=load_pk)
        context = {
            "restart": get_restart_notice,
            'release': get_version_json(),
            "title": "Load Details",
            # todo: figure out this blurb link.
            # "blurb": get_page_blurb_override('load_data/load_detail/NOT-FOUND'),
            'selected_hand_load': selected_hand_load,
            "copy_year": datetime.now().year
        }
        return render(request, "loaddata/load_details.html", context)
    except ObjectDoesNotExist:
        context = {
            "restart": get_restart_notice,
            'load_id': load_pk,
            'release': get_version_json(),
            "title": "Can't get detail without a valid id.",
            # todo: figure out this blurb link.
            # "blurb": get_page_blurb_override('load_data/load_detail/NOT-FOUND'),
            "copy_year": datetime.now().year,
        }
        return render(request, "loaddata/load_details.html", context)


def page_estimated_dope(request, load_pk='3'):
    try:
        selected_load = EstimatedDope.objects.get(hand_load=load_pk)
        context = {
            "restart": get_restart_notice,
            'load_id': load_pk,
            'release': get_version_json(),
            "title": "Estimated Dope",
            # "blurb": "I'll move it to a database setup in a bit.",
            "blurb": get_page_blurb_override('load_data/estimated_dope/'),
            'load_details': selected_load,
            "copy_year": datetime.now().year,
        }
    except ObjectDoesNotExist:
        context = {
            "restart": get_restart_notice,
            'load_id': load_pk,
            'release': get_version_json(),
            "title": "Master Po Load Data",
            "blurb": get_page_blurb_override('load_data/estimated_dope/NO-DOPE-FOUND/'),
            "copy_year": datetime.now().year,
        }

    return render(request, "loaddata/estimated_dope.html", context)


def page_firearm_detail(request, firearm_pk=None):
    if firearm_pk is None:
        context = {
            "restart": get_restart_notice,
            'load_id': firearm_pk,
            'release': get_version_json(),
            "title": "Can't get detail without an id.",
            "blurb": get_page_blurb_override('load_data/firearm_detail/NOT-FOUND'),
            "copy_year": datetime.now().year,
        }
        return render(request, "loaddata/firearm_details.html", context)
    try:
        selected_firearm = Firearm.objects.get(pk=firearm_pk)

        context = {
            "restart": get_restart_notice,
            'firearm_id': firearm_pk,
            'release': get_version_json(),
            "title": "Firearm Detail",
            # "blurb": "Sometimes knowing your tool is more important than using it quickly.",
            "blurb": get_page_blurb_override('load_data/firearm_detail/'),
            'firearm_details': selected_firearm,
            "copy_year": datetime.now().year,
        }
    except ObjectDoesNotExist:
        context = {
            "restart": get_restart_notice,
            'load_id': firearm_pk,
            'release': get_version_json(),
            "title": "OOPS! Firearm not found.",
            "blurb": get_page_blurb_override('load_data/firearm_detail/NOT-FOUND'),
            "copy_year": datetime.now().year,
        }

    return render(request, "loaddata/firearm_details.html", context)


def sample(request):
    data = {
        "restart": get_restart_notice,
        'Query': 'Complete',
        'Result': 'The query completed but this is not an endpoint with data.'
    }
    return JsonResponse(data)

# /data/django/IMRUnicorn-Django/
