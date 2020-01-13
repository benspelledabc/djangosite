from datetime import datetime
from django.conf import settings
from django.db.models import F, FloatField, ExpressionWrapper
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import os
import json


# Create your views here.
def page_home(request):
    context = {
        'release': get_version_json(request),
        "title": "Master Po (2.0) Load Data",
        "blurb": "I'll move it to a database setup in a bit.",
        "table_data": 'This should be from the database... jackle.',
        "year": datetime.now().year
    }
    return render(request, "imrunicorn/index.html", context)


def get_version_json(request):
    # data = open('release.json').read()  # opens the json file and saves the raw contents
    data = open(os.path.join(settings.BASE_DIR, 'release.json')).read()
    json_data = json.loads(data)  # converts to a json structure
    return json_data


def handler404(request, exception):
    context = {
        'release': get_version_json(request),
        "title": "Page Not Found",
        "blurb": "The requested page wasn't found. (404)",
        "fullbody": "",
        "year": datetime.now().year
    }
    # going to try sending an email on 404 error.. hahaha bad idea in production
    # self.email_test(request)

    return render(request, "errors/error.html", context)


def handler500(request):
    # return HttpResponse("Hello world 500.")
    context = {
        'release': get_version_json(request),
        "title": "Page Not Found",
        "blurb": "The requested page wasn't found. (500)",
        "fullbody": "",
        "year": datetime.now().year
    }
    return render(request, "errors/error.html", context)


def page_days_since(request):
    input_date = request.GET.get('input_date')

    batf_data = fetch_estimated_batf_days()
    check_cashed = batf_data['check_cashed']
    approved = batf_data['approved']
    stamp_received = batf_data['stamp_received']
    total = batf_data['total']



    context = {
        # 'batf_data': total_batf['check_cashed'],
        'batf_check_cashed': check_cashed,
        'batf_approved': approved,
        'batf_stamp_received': stamp_received,
        'batf_total': total,
        'release': get_version_json(request),
        "title": "Master Po (2.0) Load Data",
        "blurb": "I'll move it to a database setup in a bit.",
        "table_data": 'This should be from the database... jackle.',
        "input_date": input_date,
        "year": datetime.now().year
    }
    return render(request, "imrunicorn/days_since.html", context)


def fetch_estimated_batf_days():
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
        'check_cashed': first_number,
        'approved': second_number,
        'stamp_received': third_number,
        'total': total,
    }

    # return HttpResponse(total)
    # return JsonResponse(batf_data)
    # return JsonResponse(total, safe=False)
    # return batf_data[total]
    return batf_data
    # return total


def page_blog_add(request):
    context = {
        'body': 'no body to share',
        'header': 'add',
    }
    return JsonResponse(context)


def page_blog_read(request):
    context = {
        'body': 'no body to share',
        'header': 'read',
    }
    return JsonResponse(context)
