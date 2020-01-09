from datetime import datetime
from django.conf import settings
from django.db.models import F, FloatField, ExpressionWrapper
from django.http import JsonResponse
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

