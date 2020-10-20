import json
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Video, PicturesForCarousel


def get_dnd5e_by_pk(video_pk='1'):
    result = Video.objects.filter(
        Q(pk=video_pk)
    )
    return result


def get_all_dnd5e():
    result = Video.objects.filter()\
        .order_by('-pk', '-file_title', '-file_name')
    return result


# Video Functions
def get_video_by_pk(video_pk='1'):
    result = Video.objects.filter(
        Q(pk=video_pk)
    )
    return result


def get_all_videos():
    result = Video.objects.filter()\
        .order_by('-pk', '-file_title', '-file_name')
    return result


def get_latest_video():
    result = Video.objects.filter()\
        .order_by('-pk')[0:1]
    return result


# carousel functions
def get_all_pictures_for_carousel():
    result = PicturesForCarousel.objects.filter()\
        .order_by('-pk')
    return result


def get_recent_pictures_for_carousel():
    result = PicturesForCarousel.objects.filter()\
        .order_by('-pk')[0:3]
    return result
