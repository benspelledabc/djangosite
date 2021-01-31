from django.shortcuts import render
from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, \
    get_page_blurb_override, get_restart_notice
from imrunicorn.functions import step_hit_count_by_page
from datetime import datetime
from content_collection.functions import get_all_videos, get_latest_video, get_video_by_pk, \
    get_recent_pictures_for_carousel, get_all_pictures_for_carousel, get_all_dnd5e, get_all_fantasy_grounds
from django.shortcuts import render
from imrunicorn.decorators import allowed_groups


# Create your views here.
def page_blank(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Call Of The Wild: Blank",
        "blurb": get_page_blurb_override('call_of_the_wild/blank/'),
    }
    return render(request, "call_of_the_wild/blank.html", context)


def page_need_zone_times(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Call Of The Wild: Need Zone Times",
        "blurb": get_page_blurb_override('call_of_the_wild/need_zone_times/'),
    }
    return render(request, "call_of_the_wild/need_zone_times.html", context)


def page_trophy_stats(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Call Of The Wild: Trophy Stats",
        "blurb": get_page_blurb_override('call_of_the_wild/need_zone_times/'),
    }
    return render(request, "call_of_the_wild/trophy_stats.html", context)
