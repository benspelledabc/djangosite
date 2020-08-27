from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, \
    get_page_blurb_override, get_restart_notice
from deer_harvest_logbook.functions import all_harvests, all_harvests_by_shooter
from deer_harvest_logbook.functions import harvests_by_hour_of_day, harvests_by_hour_of_day_by_sex, harvests_by_sex
from datetime import datetime
from django.contrib.auth import get_user_model
from django.shortcuts import render


User = get_user_model()
# Create your views here.


def page_all_harvests(request):
    # all_news = all_harvests # removed this variable
    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        "all_news": all_harvests,
        'release': get_version_json(),
        "title": "Deer Harvest Logbook",
        "blurb": get_page_blurb_override('deer_harvest_logbook/'),
        # "blurb": "Coming soon...",
    }
    return render(request, "deer_harvest_logbook/all_harvests.html", context)
