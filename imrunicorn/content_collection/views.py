from django.shortcuts import render
from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, \
    get_page_blurb_override, get_restart_notice
from datetime import datetime
# from django.contrib.auth import get_user_model
from django.shortcuts import render


# Create your views here.
def page_blank(request):
    context = {
        "hide_points": True,
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Content Collection: Blank",
        "blurb": get_page_blurb_override('content_collection/blank/'),
    }
    return render(request, "content_collection/blank.html", context)
