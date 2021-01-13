from datetime import datetime, timedelta
from django.conf import settings
from django.db.models import F, FloatField, ExpressionWrapper
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import os
import json
from django.contrib.auth.models import User
from .models import PageCounter, PageHideList
from announcements.get_news import get_news, get_news_sticky, get_version_json, \
    get_page_blurb_override, get_restart_notice, get_main_page_blurb
from imrunicorn.decorators import unauthenticated_user, allowed_groups
from .functions import step_hit_count_by_page, email_user, get_weather
import logging
import requests
# from django.contrib.sites.models import Site

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)


def page_api_test(request):
    # base_url = "{0}://{1}{2}".format(request.scheme, request.get_host(), request.path)
    base_url = "{0}://{1}".format(request.scheme, request.get_host())
    response = requests.get('{domain}/api/announcements/what_is_new_random_one/'.format(domain=base_url))
    geo_data = response.json()

    data = geo_data['results'][0]

    context = {
        "title": "Testing API endpoints",
        "date": data['Date'],
        "blurb": data['Blurb'],
        # "blurb": request.path,
        "body": data['Body'],
        "copy_year": datetime.now().year,
        'release': get_version_json(),
    }

    return render(request, "imrunicorn/apicall_random_news.html", context)


def page_api_weather(request):
    # r = get_weather(request, "Westminster, Md")
    r = get_weather(request)
    # print(r)
    return JsonResponse(r)


def page_qr_about(request):
    step_hit_count_by_page(request.path)
    # return HttpResponse("Hello world 500.")
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "QR: About",
        "blurb": "QR Code Link",
        "copy_year": datetime.now().year
    }

    # i dont want to do it this way, for the purpose of demonstrating a paragraph seperation.
    # body = ["This is paragraph 1.", "This is paragraph 2.", "This is paragraph 3.", "This is paragraph 4.",
    #         "This is paragraph 5.", "This is paragraph 6.", "This is paragraph 7."]

    body = []
    body.append("There isn't much to it, but you've found a magical email! Let me know and you'll win a prize!")

    user = User.objects.get(username=request.user.username)
    if len(user.email) > 2:
        email_user(user.email, "Magical Email!", body)
    else:
        logger.error("{0}'s address is not long enough ['{1}']".format(user.username, user.email))

    return render(request, "imrunicorn/qr-about.html", context)


def page_access_denied_groups(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Access Denied",
        "deny_message": "You are not in one of the groups that is allowed to see the page requested.",
        "copy_year": datetime.now().year
    }

    body = []
    body.append("If you believe you should have had access to a page you recently visited, please reply and let me "
                "know.")

    user = User.objects.get(username=request.user.username)
    if len(user.email) > 2:
        email_user(user.email, "Access Denied: Appeal Process", body)
    else:
        logger.error("{0}'s address is not long enough ['{1}']".format(user.username, user.email))

    return render(request, "imrunicorn/access_denied.html", context)


@allowed_groups(allowed_groupname_list=['site_tester'])
def page_greyscale_test(request):
    step_hit_count_by_page(request.path)
    # return HttpResponse("Hello world 500.")
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Donate: Steel Targets",
        "blurb": "Steel targets are a resource that needs to be replaced over time.",
        "full_body": "Donate new or slightly used steel targets. "
                     "Email me at <a href=\"mailto:Admin@BenSpelledABC.me\">Admin@BenSpelledABC.me</a> and "
                     "I'll provide an address or meet in person. ",
        "copy_year": datetime.now().year
    }
    return render(request, "imrunicorn/gs_single.html", context)


# Create your views here.
def page_home(request):
    # logger.error("Test, main page hit: page_home view!!")
    step_hit_count_by_page(request.path)

    try:
        all_news = get_news_sticky()
    except IndexError as ie:
        print(ie)
    except Exception as err:
        print(err)

    try:
        main_blurb = get_main_page_blurb()
    except IndexError as ie:
        print(ie)
    except Exception as err:
        print(err)

    release = get_version_json()
    title = release['application_title']
    cut = release['cut']

    weather = get_weather(request)

    context = {
        "weather": weather,
        "main_blurb": main_blurb,
        "restart": get_restart_notice,
        "all_news": all_news,
        'release': release,
        "title": title,
        "cut": cut,
        # "blurb": get_main_page_blurb,
        "blurb": get_page_blurb_override('/'),
        "copy_year": datetime.now().year
    }
    return render(request, "imrunicorn/index.html", context)


def handler403(request, exception):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Access Denied",
        "subtitle": "Friendly 403 error message.",
        "fullbody": "",
        "copy_year": datetime.now().year
    }
    # return render(request, "errors/403-denied.html", context)
    return render(request, "errors/403-gs-error.html", context)


def handler404(request, exception):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Page Not Found",
        "blurb": "The requested page wasn't found. (404)",
        "fullbody": "",
        "copy_year": datetime.now().year
    }
    # going to try sending an email on 404 error.. hahaha bad idea in production
    # self.email_test(request)

    return render(request, "errors/error.html", context)


def handler500(request):
    step_hit_count_by_page(request.path)
    # return HttpResponse("Hello world 500.")
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Page Not Found",
        "blurb": "The requested page wasn't found. (500)",
        "fullbody": "",
        "copy_year": datetime.now().year
    }
    return render(request, "errors/error.html", context)


def page_cash_app(request):
    # return HttpResponse("Hello world 500.")
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "cash_app": "Show_QR_Code",
        "title": "Donate: Cash App",
        "blurb": "Cash app is our preferred method of making and receiving payment.",
        "full_body": "",
        "copy_year": datetime.now().year
    }
    return render(request, "imrunicorn/donate_cash_app.html", context)


def page_page_hits(request):
    step_hit_count_by_page(request.path)
    page_hits = PageCounter.objects.\
        exclude(page_name__in=PageHideList.objects.values('page_name')).order_by('-page_hit_count')

    page_hits = PageCounter.objects.exclude(
        page_name__in=PageHideList.objects.values('page_name'),
    ).order_by('-page_hit_count')

    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Hot Pages",
        "blurb": "See what others are looking at.",
        "page_hits": page_hits,
        "copy_year": datetime.now().year
    }
    return render(request, "imrunicorn/page_hits.html", context)


def page_donate_steel_targets(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Donate: Steel Targets",
        "blurb": "Steel targets are a resource that needs to be replaced over time.",
        "full_body": "Donate new or slightly used steel targets. "
                     "Email me at <a href=\"mailto:Admin@BenSpelledABC.me\">Admin@BenSpelledABC.me</a> and "
                     "I'll provide an address or meet in person. ",
        "copy_year": datetime.now().year
    }
    return render(request, "imrunicorn/simple_use_variables.html", context)


def page_days_since(request):
    step_hit_count_by_page(request.path)
    input_date = request.GET.get('input_date')

    blurb_string = "/days_since?input_date=" + input_date

    batf_data = fetch_estimated_batf_days()
    check_cashed = batf_data['check_cashed']
    approved = batf_data['approved']
    stamp_received = batf_data['stamp_received']
    total = batf_data['total']
    cached_result = batf_data['cached_result']

    context = {
        "restart": get_restart_notice,
        # 'batf_data': total_batf['check_cashed'],
        'cached_result': cached_result,
        'batf_check_cashed': check_cashed,
        'batf_approved': approved,
        'batf_stamp_received': stamp_received,
        'batf_total': total,
        'release': get_version_json(),
        "title": "Days since " + input_date,
        "blurb": get_page_blurb_override(blurb_string),
        "input_date": input_date,
        "copy_year": datetime.now().year
    }
    return render(request, "imrunicorn/days_since.html", context)


def fetch_estimated_batf_days():
    # step_hit_count_by_page(request.path)
    try:
        import requests
        url = 'https://www.silencershop.com/atf-wait-times'
        response = requests.get(url)
        # F4 Individual - Paper\"},{\"v\":32},{\"v\":175},{\"v\":10}]},{\"c\

        stop_before = response.text.find('F4 Individual - EFile')
        stop_after = response.text.find('F4 Individual - Paper')

        # getting there.. this is the right SECTION but we need to split it up more
        answer = response.text[stop_after:stop_before]
        answer_pieces = answer.split(':')

        # first_number is correct
        first_number_pieces = answer_pieces[1].split('}')
        first_number = int(first_number_pieces[0])

        # second number starts around here
        second_number_pieces = answer_pieces[2].split('}')
        second_number = int(second_number_pieces[0])

        # third number starts around here
        third_number_pieces = answer_pieces[3].split('}')
        third_number = int(third_number_pieces[0])

        total = first_number + second_number + third_number

        batf_data = {
            'cached_result': False,
            'check_cashed': first_number,
            'approved': second_number,
            'stamp_received': third_number,
            'total': total,
        }

    except ConnectionError:
        batf_data = {
            'cached_result': True,
            'check_cashed': 32,
            'approved': 175,
            'stamp_received': 10,
            'total': 217,
        }
        # todo: make this not complain
    except Exception:
        batf_data = {
            'cached_result': True,
            'check_cashed': 32,
            'approved': 175,
            'stamp_received': 10,
            'total': 217,
        }

    return batf_data


def page_blog_add(request):
    step_hit_count_by_page(request.path)
    context = {
        "restart": get_restart_notice,
        'body': 'no body to share',
        'header': 'add',
    }
    return JsonResponse(context)


def page_blog_read(request):
    step_hit_count_by_page(request.path)
    context = {
        'body': 'no body to share',
        'header': 'add',
    }
    return JsonResponse(context)


def page_pi_endpoint(request):
    step_hit_count_by_page(request.path)
    context = {
        'header': 'I like small holes...',
        'body': 'This is a lightweight endpoint to test the raspberry pi.',
    }
    return JsonResponse(context)
