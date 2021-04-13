import urllib

import requests
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser

from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, \
    get_page_blurb_override, get_restart_notice
from imrunicorn.functions import step_hit_count_by_page
from datetime import datetime
from content_collection.functions import get_all_videos, get_latest_video, get_video_by_pk, \
    get_recent_pictures_for_carousel, get_all_pictures_for_carousel, get_all_dnd5e, \
    get_all_fantasy_grounds, get_all_insults
# from django.contrib.auth import get_user_model
from django.shortcuts import render
from imrunicorn.decorators import allowed_groups
# @allowed_groups(allowed_groupname_list=['admin_tools_members'])
# request.user.groups.filter(name__in=allowed_groupname_list).exists()
from .serializer import RandomInsultSerializer


def insult_list_all(request):
    # return HttpResponse("hello world")

    # get the list of todos
    # response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    # transfer the response to json objects
    # todos = response.json()   # send todos in context... BAM

    step_hit_count_by_page(request.path)
    insults = get_all_insults

    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Content Collection: Insult",
        "insults": insults,
        "blurb": get_page_blurb_override('content_collection/insult/'),
    }
    return render(request, "content_collection/insult_list_all.html", context)


def leach_insult(request):
    step_hit_count_by_page(request.path)
    output = "I failed to get data."
    try:
        url = "https://www.kassoon.com/dnd/vicious-mockery-insult-generator/"
        page = urllib.request.urlopen(url)
        content = page.read().decode()
        content_parts = content.split("</p><p>OR</p><p>")
        testing = content_parts[1]
        testing_bits = testing.split("</p>")
        output = testing_bits[0]
    except Exception as ex:
        print("Exception: {0}".format(ex))

    my_obj = {'insult': output}
    status_code_message = ""
    try:
        insult_serializer = RandomInsultSerializer(data=my_obj)
        if insult_serializer.is_valid():
            insult_serializer.save()
            status_code_message = "Saved newly generated insult to database."
    except Exception as ex:
        print(ex)

    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Content Collection: Insult",
        "insult": output,
        "status_code_message": status_code_message,
        "blurb": get_page_blurb_override('content_collection/insult/'),
    }
    return render(request, "content_collection/insult.html", context)


def page_home(request):
    step_hit_count_by_page(request.path)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Content Collection: Home",
        "blurb": get_page_blurb_override('content_collection/home/'),
    }
    return render(request, "content_collection/home.html", context)


# Create your views here.
def page_blank(request):
    step_hit_count_by_page(request.path)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Content Collection: Blank",
        "blurb": get_page_blurb_override('content_collection/blank/'),
    }
    return render(request, "content_collection/blank.html", context)


# @allowed_groups(allowed_groupname_list=['content_collection_fantasy_grounds'])
# @permission_required('content_collection.view_fantasygrounds', login_url='/login', raise_exception=True)
def page_fantasy_grounds_list(request):
    step_hit_count_by_page(request.path)
    item_list = get_all_fantasy_grounds()

    perm_check = request.user.has_perm('content_collection.view_fantasygrounds')
    unrestricted = perm_check

    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Fantasy Grounds",
        "item_list": item_list,
        "blurb": get_page_blurb_override('content_collection/dnd5e/'),
    }
    return render(request, "content_collection/dnd5e.html", context)


# @allowed_groups(allowed_groupname_list=['content_collection_dnd5e'])
# @permission_required('content_collection.view_DAndDFifthEditionBook', login_url='/login', raise_exception=True)
def page_dnd5e_list(request):
    step_hit_count_by_page(request.path)
    item_list = get_all_dnd5e()

    perm_check = request.user.has_perm('content_collection.view_danddfiftheditionbook')
    unrestricted = perm_check

    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "D&D-5e",
        "item_list": item_list,
        "unrestricted_user": unrestricted,
        "blurb": get_page_blurb_override('content_collection/dnd5e/'),
    }
    return render(request, "content_collection/dnd5e.html", context)


# @permission_required('content_collection.view_PicturesForCarousel', login_url='/login', raise_exception=True)
def page_carousel_recent(request):
    step_hit_count_by_page(request.path)
    carousel = get_recent_pictures_for_carousel()

    perm_check = request.user.has_perm('content_collection.view_picturesforcarousel')
    unrestricted = perm_check

    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Carousel: Recent",
        'unrestricted_user': unrestricted,
        "carousel": carousel,
        "blurb": get_page_blurb_override('content_collection/carousel/recent/'),
    }
    return render(request, "content_collection/carousel.html", context)


# @permission_required('content_collection.view_PicturesForCarousel', login_url='/login', raise_exception=True)
def page_carousel(request):
    step_hit_count_by_page(request.path)
    carousel = get_all_pictures_for_carousel()

    perm_check = request.user.has_perm('content_collection.view_picturesforcarousel')
    unrestricted = perm_check

    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Carousel (All)",
        'unrestricted_user': unrestricted,
        "carousel": carousel,
        "blurb": get_page_blurb_override('content_collection/carousel/'),
    }
    return render(request, "content_collection/carousel.html", context)


# @permission_required('content_collection.view_Video', login_url='/login', raise_exception=True)
def page_latest_video_by_pk(request, video_pk=1):
    step_hit_count_by_page(request.path)
    videos = get_video_by_pk(video_pk)

    perm_check = request.user.has_perm('content_collection.view_video')
    unrestricted = perm_check

    context = {
        "videos": videos,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        'unrestricted_user': unrestricted,
        "title": "Videos: #{video_id}".format(video_id=video_pk),
        "blurb": get_page_blurb_override('content_collection/videos/'),
    }
    return render(request, "content_collection/videos.html", context)


# @permission_required('content_collection.view_Video', login_url='/login', raise_exception=True)
def page_latest_video(request):
    step_hit_count_by_page(request.path)
    videos = get_latest_video

    perm_check = request.user.has_perm('content_collection.view_video')
    unrestricted = perm_check

    context = {
        "videos": videos,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Videos: Latest",
        'unrestricted_user': unrestricted,
        "blurb": get_page_blurb_override('content_collection/videos/'),
    }
    return render(request, "content_collection/videos.html", context)


# @permission_required('content_collection.view_Video', login_url='/login', raise_exception=True)
def page_video_list(request):
    step_hit_count_by_page(request.path)
    videos = get_all_videos

    perm_check = request.user.has_perm('content_collection.view_video')
    unrestricted = perm_check

    context = {
        "videos": videos,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        'unrestricted_user': unrestricted,
        "title": "Video List",
        "blurb": get_page_blurb_override('content_collection/videos_list/'),
    }
    return render(request, "content_collection/video_list.html", context)


# @permission_required('content_collection.view_Video', login_url='/login', raise_exception=True)
def page_videos(request):
    step_hit_count_by_page(request.path)
    videos = get_all_videos

    perm_check = request.user.has_perm('content_collection.view_video')
    unrestricted = perm_check

    context = {
        "videos": videos,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        'unrestricted_user': unrestricted,
        "title": "Videos: All (slow to load)",
        "blurb": get_page_blurb_override('content_collection/videos/'),
    }
    return render(request, "content_collection/videos.html", context)
