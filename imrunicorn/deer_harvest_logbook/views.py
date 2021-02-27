from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, \
    get_page_blurb_override, get_restart_notice
from imrunicorn.functions import step_hit_count_by_page
from deer_harvest_logbook.functions import all_harvests, all_harvests_by_shooter
from deer_harvest_logbook.functions import harvests_by_hour_of_day, harvests_by_score, harvests_by_sex
from datetime import datetime
from django.contrib.auth import get_user_model
from django.shortcuts import render


User = get_user_model()


def page_charts(request):
    step_hit_count_by_page(request.path)
    logs = harvests_by_hour_of_day()
    logs_sexy = harvests_by_sex()
    logs_by_score = harvests_by_score()
    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        "logs": logs,
        "logs_sexy": logs_sexy,
        "logs_sexy_hour": logs_by_score,
        'release': get_version_json(),
        "title": "Harvest Charts",
        "blurb": get_page_blurb_override('deer_harvest_logbook/charts/'),
    }
    return render(request, "deer_harvest_logbook/harvest_charts.html", context)


def page_point_system(request):
    step_hit_count_by_page(request.path)
    context = {
        "hide_points": True,
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Deer Harvest Point System",
        "blurb": get_page_blurb_override('deer_harvest_logbook/point_system/'),
    }
    return render(request, "deer_harvest_logbook/point_system.html", context)


def page_point_system_show_points(request):
    step_hit_count_by_page(request.path)
    context = {
        "hide_points": False,
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Deer Harvest Point System",
        "blurb": get_page_blurb_override('deer_harvest_logbook/point_system/'),
    }
    return render(request, "deer_harvest_logbook/point_system.html", context)


def page_all_harvests(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        "all_news": all_harvests(request),
        'release': get_version_json(),
        "title": "Deer Harvest Logbook",
        "blurb": get_page_blurb_override('deer_harvest_logbook/'),
    }
    return render(request, "deer_harvest_logbook/all_harvests.html", context)


def page_all_harvests_by_shooter_pk(request, shooter_pk=1):
    step_hit_count_by_page(request.path)
    # all_news = all_groundhog_removals_by_shooter(shooter_pk)
    all_news = all_harvests
    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        "all_news": all_news,
        'release': get_version_json(),
        "title": "Deer Harvest Logbook",
        "blurb": get_page_blurb_override('deer_harvest_logbook/by_shooter/'),
    }
    return render(request, "deer_harvest_logbook/all_harvests.html", context)
