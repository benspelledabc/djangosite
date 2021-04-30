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
from .functions import leach_post, leach_post_subreddit, get_meme_list

import logging
# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)


def page_meme_by_subreddit(request, subreddit):
    step_hit_count_by_page(request.path)
    meme = leach_post_subreddit(subreddit)
    print(meme)     # {'code': 404, 'message': "This subreddit has no posts or doesn't exist."}
    buffer = {}
    try:
        if meme['code'] == 404:
            buffer['subreddit'] = subreddit
            buffer['title'] = "This subreddit has no posts or doesn't exist. Here's a random picsum picture."
            buffer['url'] = "https://picsum.photos/400"
            meme = buffer
    except KeyError as key_error:
        print("We found a key_error, because it has valid data!")

    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Meme Leach: {0}".format(subreddit),
        "meme": meme,
        "blurb": get_page_blurb_override('meme_leach/fetch'),
    }
    return render(request, "meme_leach/subreddit.html", context)


def page_meme(request):
    step_hit_count_by_page(request.path)
    meme = leach_post()
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Meme Leach",
        "meme": meme,
        "blurb": get_page_blurb_override('meme_leach/fetch'),
    }
    return render(request, "meme_leach/subreddit.html", context)


def page_sfw_meme_list(request):
    step_hit_count_by_page(request.path)
    memes = get_meme_list(request, False)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Meme List",
        "memes": memes,
        "blurb": get_page_blurb_override('meme_leach/'),
    }
    return render(request, "meme_leach/list.html", context)


@permission_required('meme_leach.view_leachedmeme', login_url='/login', raise_exception=True)
def page_nsfw_meme_list(request):
    step_hit_count_by_page(request.path)
    memes = get_meme_list(request, True)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Meme List",
        "memes": memes,
        "blurb": get_page_blurb_override('meme_leach/'),
    }
    return render(request, "meme_leach/nsfw-list.html", context)
