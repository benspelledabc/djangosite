import urllib
from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
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
    get_all_fantasy_grounds, get_all_insults, get_all_secrets, get_all_buzz_words_or_phrases, get_sketch_by_pk, \
    get_all_sketches

# from django.contrib.auth import get_user_model
from django.shortcuts import render
from imrunicorn.decorators import allowed_groups
# @allowed_groups(allowed_groupname_list=['admin_tools_members'])
# request.user.groups.filter(name__in=allowed_groupname_list).exists()
from .models import SensorReadings
from .serializer import RandomInsultSerializer, SensorReadingsSerializer


def buzz_words_or_phrases_list_all(request):
    step_hit_count_by_page(request.path)
    words = get_all_buzz_words_or_phrases()

    new_entries = words['new_entries']

    word_list = words['result']
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Content Collection: Buzz Words (or Phrases)",
        "words": word_list,
        "new_words_or_phrases": new_entries,
        "blurb": get_page_blurb_override('content_collection/buzz_words_or_phrases_list_all/'),
    }
    return render(request, "content_collection/buzz_words_or_phrases_list_all.html", context)


@permission_required('content_collection.view_secrets', login_url='/login', raise_exception=True)
def secrets_list_all(request):
    step_hit_count_by_page(request.path)
    secrets = get_all_secrets

    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Content Collection: Secrets",
        "secrets": secrets,
        "blurb": get_page_blurb_override('content_collection/secrets_list_all/'),
    }
    return render(request, "content_collection/secrets_list_all.html", context)


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


# todo: make a buzzword generator!
# https://www.robietherobot.com/buzzword.htm

def leach_insult(request):
    step_hit_count_by_page(request.path)
    insult_one = "I failed to get data."
    insult_two = "I failed to get data."
    try:
        url = "https://www.kassoon.com/dnd/vicious-mockery-insult-generator/"
        page = urllib.request.urlopen(url)
        content = page.read().decode()
        content_parts = content.split("</p><p>OR</p><p>")

        # get insult one
        core_part_one = content_parts[0]
        insult_one = core_part_one[core_part_one.rindex('<p>')+4:]

        # get the second insult on the page
        core_part_two = content_parts[1]
        core_part_two_bits = core_part_two.split("</p>")
        insult_two = core_part_two_bits[0]

    except Exception as ex:
        print("Exception: {0}".format(ex))

    # save the insults
    saved_insult_count = 0

    # save the first insult
    insult = {'insult': insult_one}
    status_code_message = ""
    try:
        insult_serializer = RandomInsultSerializer(data=insult)
        if insult_serializer.is_valid():
            insult_serializer.save()
            status_code_message = "Saved newly generated insult to database."
            saved_insult_count += 1
    except Exception as ex:
        print(ex)

    # save the second insult
    insult = {'insult': insult_two}
    status_code_message = ""
    try:
        insult_serializer = RandomInsultSerializer(data=insult)
        if insult_serializer.is_valid():
            insult_serializer.save()
            status_code_message = "Saved newly generated insult to database."
            saved_insult_count += 1
    except Exception as ex:
        print(ex)

    # insult = [insult_one, insult_two]
    if saved_insult_count == 0:
        status_code_message = ""
    elif saved_insult_count == 1:
        status_code_message = "Saved newly generated insult to database."
    elif saved_insult_count == 2:
        status_code_message = "Saved two newly generated insults to database."
    else:
        status_code_message = "Something went terribly wrong."

    insults = [insult_one, insult_two]

    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Content Collection: Insult",
        "insults": insults,
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
@permission_required('content_collection.view_danddfiftheditionbook', login_url='/login', raise_exception=True)
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


# ############### Raspberry Pi Hook ############
@api_view(['GET', 'POST'])
def sensor_readings(request):
    step_hit_count_by_page(request.path)
    perm_check = request.user.has_perm('content_collection.change_sensorreadings')

    if request.method == 'POST':
        if perm_check:
            try:
                data_of_value = {'sensor_location': request.data.get('sensor_location'),
                                 'sensor_model': request.data.get('sensor_model'),
                                 'celsius': request.data.get('celsius'),
                                 'fahrenheit': request.data.get('fahrenheit'),
                                 'humidity': request.data.get('humidity')
                                 }

                serializer = SensorReadingsSerializer(data=data_of_value)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as ex:
                return JsonResponse({"status": "error", "exception": ex})
        else:
            return JsonResponse({"access": "denied", "permission_required": "content_collection.change_sensorreadings"})
    else:
        # assume its a get, limit it to 30 for now until pagination is fixed
        queryset = SensorReadings.objects.all().order_by('-read_datetime')[:30]
        serializer = SensorReadingsSerializer(queryset, many=True, context=request)
        return Response(serializer.data)


def sensor_readings_test(request):
    step_hit_count_by_page(request.path)
    perm_check = request.user.has_perm('content_collection.change_sensorreadings')

    if request.method == 'POST':
        if perm_check:
            try:
                data_of_value = {'sensor_location': request.data.get('sensor_location'),
                                 'sensor_model': request.data.get('sensor_model'),
                                 'celsius': request.data.get('celsius'),
                                 'fahrenheit': request.data.get('fahrenheit'),
                                 'humidity': request.data.get('humidity')
                                 }

                serializer = SensorReadingsSerializer(data=data_of_value)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as ex:
                return JsonResponse({"status": "error", "exception": ex})
        else:
            return JsonResponse({"access": "denied", "permission_required": "content_collection.change_sensorreadings"})
    else:
        # assume its a get, limit it to 30 for now until pagination is fixed
        queryset = SensorReadings.objects.all().order_by('-read_datetime')[:30]
        serializer = SensorReadingsSerializer(queryset, many=True, context=request)
        return Response(serializer.data)


def page_sketch_by_pk(request, sketch_pk=1):
    step_hit_count_by_page(request.path)
    sketch = get_sketch_by_pk(sketch_pk)

    blurb = get_page_blurb_override('content_collection/sketches/')   # default blurb override
    unrestricted = False
    has_permission = False
    special_permission = 'Content_Collection.View_ArduinoUnoSketch'
    has_permission = request.user.has_perm(special_permission.lower())

    if sketch[0].restricted:
        if has_permission:
            unrestricted = True
            blurb = sketch[0].title
        else:
            blurb = "Sketch title hidden due to access reasons."
    else:
        unrestricted = True
        blurb = sketch[0].title

    context = {
        "sketch": sketch,
        "special_permission": special_permission,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        'unrestricted_user': unrestricted,
        "title": "Sketch: #{sketch_pk}".format(sketch_pk=sketch_pk),
        "blurb": blurb,
    }
    return render(request, "content_collection/sketch.html", context)


def page_sketch_list(request):
    step_hit_count_by_page(request.path)
    sketches = get_all_sketches

    perm_check = request.user.has_perm('content_collection.view_arduinounosketch')
    unrestricted = perm_check

    context = {
        "sketches": sketches,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        'unrestricted_user': unrestricted,
        "title": "Sketch List",
        "blurb": get_page_blurb_override('content_collection/sketches/'),
    }
    return render(request, "content_collection/sketches_list.html", context)
