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
        "title": "Activity Log: Blank",
        "blurb": get_page_blurb_override('activity_log/blank/'),
    }
    return render(request, "activity_log/blank.html", context)
