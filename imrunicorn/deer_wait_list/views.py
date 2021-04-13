from django.shortcuts import render
from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, \
    get_page_blurb_override, get_restart_notice
from imrunicorn.functions import step_hit_count_by_page
from .functions import get_all_orders, get_remaining_orders, get_all_flavors, get_all_cuts
from datetime import datetime
from django.shortcuts import render


def page_blank(request):
    step_hit_count_by_page(request.path)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Deer Wait List: Blank",
        "blurb": get_page_blurb_override('deer_wait_list/blank/'),
    }
    return render(request, "deer_wait_list/blank.html", context)


def page_info(request):
    step_hit_count_by_page(request.path)
    cuts = get_all_cuts()
    flavors = get_all_flavors()
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "cuts": cuts,
        "flavors": flavors,
        "title": "Deer Wait List: Info",
        "blurb": get_page_blurb_override('deer_wait_list/info/'),
    }
    return render(request, "deer_wait_list/info.html", context)


def page_list_view(request):
    step_hit_count_by_page(request.path)
    orders = get_remaining_orders()

    # todo: fix up the permissions to prevent group name requirements
    unrestricted = False
    allowed_groupname_list = ['deer_wait_list_perceived_thankfulness_viewer']
    if request.user.groups.filter(name__in=allowed_groupname_list).exists():
        unrestricted = True

    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "orders": orders,
        "unrestricted": unrestricted,
        "title": "Deer Wait List: List View",
        "blurb": get_page_blurb_override('deer_wait_list/list_view/'),
    }
    return render(request, "deer_wait_list/list_view.html", context)
