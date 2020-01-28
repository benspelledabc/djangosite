from datetime import datetime
from django.conf import settings
from django.db.models import F, FloatField, ExpressionWrapper
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import os
import json

from announcements.get_news import get_news, get_version_json


# Create your views here.
def page_all_news(request):
    context = {
        "all_news": get_news,
        'release': get_version_json(),
        "title": "All the news",
        "news_overview": "I've decided to make a blog of sorts. It's super light for speed and readability on "
                         "cellphones. I'll expand functionality later but for now this is just a listing of the "
                         "'Announcements' published.",
        "year": datetime.now().year
    }
    return render(request, "announcements/all_news.html", context)
