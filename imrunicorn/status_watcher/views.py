from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime
from announcements.get_news import get_news, get_version_json, get_page_blurb_override, get_restart_notice
from .queries import get_watch_list
# Create your views here.


def page_view_watches_reset(request):
    watches = get_watch_list()

    for item in watches:
        # page_search = search_url_for_magic_string(item.item_link, item.item_phrase)
        item.item_exception = "reset"
        item.item_phrase_not_exist = None
        item.save()

    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Status Watcher",
        # "blurb": "This page is a place holder for what's to come soon.",
        "blurb": get_page_blurb_override('status_watcher/view_watches/'),
        'watch_list': watches,
        "copy_year": datetime.now().year
    }
    return render(request, "status_watcher/view_list.html", context)


def page_view_watches(request):
    watches = get_watch_list()

    for item in watches:
        page_search = search_url_for_magic_string(item.item_link, item.item_phrase)
        item.item_exception = page_search['exception']
        item.item_phrase_not_exist = page_search['string_found']

        item.save()

    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Status Watcher",
        # "blurb": "This page is a place holder for what's to come soon.",
        "blurb": get_page_blurb_override('status_watcher/view_watches/'),
        'watch_list': watches,
        "copy_year": datetime.now().year
    }
    return render(request, "status_watcher/view_list.html", context)


def search_url_for_magic_string(search_url, magic_string):
    try:
        import requests
        url = search_url
        response = requests.get(url)

        magic_string_found = True
        if response.text.find(magic_string) == -1:
            magic_string_found = True
        else:
            magic_string_found = False

        result = {
            'exception': 'none',
            'cached_result': False,
            'string_found': magic_string_found,
        }

    except ConnectionError as ce:
        result = {
            'exception': "Connection Error",
            'cached_result': True,
            'string_found': None,
        }

    except Exception as e:
        result = {
            'exception': "Exception",
            'cached_result': True,
            'string_found': None,
        }

    return result


# eventually, we'll remove everything below this line

def page_view_watches_lkg(request):
    watches = get_watch_list()
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Status Watcher",
        # "blurb": "This page is a place holder for what's to come soon.",
        "blurb": get_page_blurb_override('status_watcher/view_watches/'),
        'watch_list': watches,
        "copy_year": datetime.now().year
    }
    return render(request, "status_watcher/view_list.html", context)


def page_home_old(request):
    context = {
        'body': 'no body to share',
        'header': 'Status',
    }
    return JsonResponse(context)
