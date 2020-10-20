from django.shortcuts import render
from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, \
    get_page_blurb_override, get_restart_notice
from imrunicorn.functions import step_hit_count_by_page
from datetime import datetime
from content_collection.functions import get_all_videos, get_latest_video, get_video_by_pk, \
    get_recent_pictures_for_carousel, get_all_pictures_for_carousel, get_all_dnd5e, get_dnd5e_by_pk
# from django.contrib.auth import get_user_model
from django.shortcuts import render
# from imrunicorn.decorators import allowed_groups
# @allowed_groups(allowed_groupname_list=['admin_tools_members'])
# request.user.groups.filter(name__in=allowed_groupname_list).exists()


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


def page_dnd5e_list(request):
    step_hit_count_by_page(request.path)
    item_list = get_all_dnd5e()
    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Content Collection: D&D-5e",
        "item_list": item_list,
        "blurb": get_page_blurb_override('content_collection/dnd5e/'),
    }
    return render(request, "content_collection/dnd5e.html", context)


def page_dnd5e_list_by_pk(request, dnd5e_pk=1):
    step_hit_count_by_page(request.path)
    item_list = get_dnd5e_by_pk(dnd5e_pk)
    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Content Collection: D&D-5e",
        "item_list": item_list,
        "blurb": get_page_blurb_override('content_collection/dnd5e/'),
    }
    return render(request, "content_collection/dnd5e.html", context)


def page_carousel_recent(request):
    step_hit_count_by_page(request.path)
    carousel = get_recent_pictures_for_carousel()

    unrestricted = False
    allowed_groupname_list = ['content_collection_unrestricted']
    if request.user.groups.filter(name__in=allowed_groupname_list).exists():
        unrestricted = True

    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Content Collection: Carousel",
        'unrestricted_user': unrestricted,
        "carousel": carousel,
        "blurb": get_page_blurb_override('content_collection/carousel/'),
    }
    return render(request, "content_collection/carousel.html", context)


def page_carousel(request):
    step_hit_count_by_page(request.path)
    carousel = get_all_pictures_for_carousel()

    unrestricted = False
    allowed_groupname_list = ['content_collection_unrestricted']
    if request.user.groups.filter(name__in=allowed_groupname_list).exists():
        unrestricted = True

    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Content Collection: Carousel",
        'unrestricted_user': unrestricted,
        "carousel": carousel,
        "blurb": get_page_blurb_override('content_collection/carousel/'),
    }
    return render(request, "content_collection/carousel.html", context)


def page_latest_video_by_pk(request, video_pk=1):
    step_hit_count_by_page(request.path)
    videos = get_video_by_pk(video_pk)

    unrestricted = False
    allowed_groupname_list = ['content_collection_unrestricted']
    if request.user.groups.filter(name__in=allowed_groupname_list).exists():
        unrestricted = True

    context = {
        "videos": videos,
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        'unrestricted_user': unrestricted,
        "title": "Videos: #{video_id}".format(video_id=video_pk),
        "blurb": get_page_blurb_override('content_collection/videos/'),
    }
    return render(request, "content_collection/videos.html", context)


def page_latest_video(request):
    step_hit_count_by_page(request.path)
    videos = get_latest_video

    unrestricted = False
    allowed_groupname_list = ['content_collection_unrestricted']
    if request.user.groups.filter(name__in=allowed_groupname_list).exists():
        unrestricted = True

    context = {
        "videos": videos,
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Videos: Latest",
        'unrestricted_user': unrestricted,
        "blurb": get_page_blurb_override('content_collection/videos/'),
    }
    return render(request, "content_collection/videos.html", context)


def page_video_list(request):
    step_hit_count_by_page(request.path)
    videos = get_all_videos

    unrestricted = False
    allowed_groupname_list = ['content_collection_unrestricted']
    if request.user.groups.filter(name__in=allowed_groupname_list).exists():
        unrestricted = True

    context = {
        "videos": videos,
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        'unrestricted_user': unrestricted,
        "title": "Video List",
        "blurb": get_page_blurb_override('content_collection/videos_list/'),
    }
    return render(request, "content_collection/video_list.html", context)


def page_videos(request):
    step_hit_count_by_page(request.path)
    videos = get_all_videos

    unrestricted = False
    allowed_groupname_list = ['content_collection_unrestricted']
    if request.user.groups.filter(name__in=allowed_groupname_list).exists():
        unrestricted = True

    context = {
        "videos": videos,
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        'unrestricted_user': unrestricted,
        "title": "Videos: All (slow to load)",
        "blurb": get_page_blurb_override('content_collection/videos/'),
    }
    return render(request, "content_collection/videos.html", context)
