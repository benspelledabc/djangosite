from django.shortcuts import render
from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, \
    get_page_blurb_override, get_restart_notice
from datetime import datetime
from content_collection.functions import get_all_videos, get_latest_video, get_video_by_pk
# from django.contrib.auth import get_user_model
from django.shortcuts import render


# Create your views here.
def page_blank(request):
    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Content Collection: Blank",
        "blurb": get_page_blurb_override('content_collection/blank/'),
    }
    return render(request, "content_collection/blank.html", context)


def page_latest_video_by_pk(request, video_pk=1):
    videos = get_video_by_pk(video_pk)
    context = {
        "videos": videos,
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Videos: #{video_id}".format(video_id=video_pk),
        "blurb": get_page_blurb_override('content_collection/videos/'),
    }
    return render(request, "content_collection/videos.html", context)


def page_latest_video(request):
    videos = get_latest_video
    context = {
        "videos": videos,
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Videos: Latest",
        "blurb": get_page_blurb_override('content_collection/videos/'),
    }
    return render(request, "content_collection/videos.html", context)


def page_video_list(request):
    videos = get_all_videos
    context = {
        "videos": videos,
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Video List",
        "blurb": get_page_blurb_override('content_collection/videos_list/'),
    }
    return render(request, "content_collection/video_list.html", context)


def page_videos(request):
    videos = get_all_videos
    context = {
        "videos": videos,
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Videos: All (slow to load)",
        "blurb": get_page_blurb_override('content_collection/videos/'),
    }
    return render(request, "content_collection/videos.html", context)
