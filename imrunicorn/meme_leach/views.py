from datetime import datetime

import requests
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.db.models import F, FloatField, ExpressionWrapper, TextField, IntegerField
from django.http import JsonResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
import os
import json
from announcements.get_news import get_news, get_version_json, get_page_blurb_override, get_restart_notice
from imrunicorn.decorators import unauthenticated_user, allowed_groups
from imrunicorn.functions import step_hit_count_by_page
from .functions import leach_post

import logging
# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)


def sample(request):
    step_hit_count_by_page(request.path)
    r = leach_post(True)

    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Zoinks",
        "blurb": get_page_blurb_override('meme_leach/'),
    }
    return render(request, "meme_leach/home.html", context)

