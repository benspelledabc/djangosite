from django.shortcuts import render
from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, \
    get_page_blurb_override, get_restart_notice
from imrunicorn.functions import step_hit_count_by_page
from .functions import get_all_orders, get_remaining_orders
from datetime import datetime
from django.shortcuts import render


def page_blank(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Deer Wait List: Blank",
        "blurb": get_page_blurb_override('deer_wait_list/blank/'),
    }
    return render(request, "deer_wait_list/blank.html", context)


def page_info(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Deer Wait List: Info",
        "blurb": get_page_blurb_override('deer_wait_list/info/'),
    }
    return render(request, "deer_wait_list/info.html", context)


def page_list_view(request):
    step_hit_count_by_page(request.path)
    orders = get_remaining_orders()
    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "orders": orders,
        "title": "Deer Wait List: List View",
        "blurb": get_page_blurb_override('deer_wait_list/list_view/'),
    }
    return render(request, "deer_wait_list/list_view.html", context)
