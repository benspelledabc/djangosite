from datetime import datetime
from django.conf import settings
from django.db.models import F, FloatField, ExpressionWrapper
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import os
import json

from announcements.get_news import get_news, get_news_sticky, get_version_json, \
    get_page_blurb_override, get_restart_notice, get_main_page_blurb


def page_greyscale_test(request):
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

    context = {
        "main_blurb": main_blurb,
        "restart": get_restart_notice,
        "all_news": all_news,
        'release': release,
        "title": title,
        # "blurb": get_main_page_blurb,
        "blurb": get_page_blurb_override('/'),
        "copy_year": datetime.now().year
    }
    return render(request, "imrunicorn/index.html", context)


def handler403(request, exception):
    context = {
        "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Access Denied",
        "subtitle": "Friendly 403 error message.",
        "fullbody": "",
        "copy_year": datetime.now().year
    }
    # going to try sending an email on 404 error.. hahaha bad idea in production
    # self.email_test(request)

    return render(request, "errors/403-denied.html", context)


def handler404(request, exception):
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


def page_donate_steel_targets(request):
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
    return render(request, "imrunicorn/simple_use_variables.html", context)


def page_days_since(request):
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
    context = {
        "restart": get_restart_notice,
        'body': 'no body to share',
        'header': 'add',
    }
    return JsonResponse(context)


def page_blog_read(request):
    context = {
        "restart": get_restart_notice,
        'body': 'no body to share',
        'header': 'add',
    }
    return JsonResponse(context)


def page_pi_endpoint(request):
    context = {
        "restart": get_restart_notice,
        'header': 'Small holes',
        'body': 'This is a lightweight endpoint to test the raspberry pi.',
    }
    return JsonResponse(context)
