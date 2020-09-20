from datetime import datetime
from django.conf import settings
from django.db.models import F, FloatField, ExpressionWrapper
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import os
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.views import APIView
from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, \
    get_version_json, get_page_blurb_override, get_restart_notice
from django.shortcuts import render
from rest_framework import viewsets

from .models import WhatIsNew, MainPageBlurbs, PageBlurbOverrides
from .serializer import NewsSerializer, MainPageBlurbsSerializer, PageBlurbOverridesSerializer

import logging

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)


# Create your views here.
def page_all_news(request):
    logger.info("This is not getting logged...")
    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        "all_news": get_news,
        'release': get_version_json(),
        "title": "All the news",
        "blurb": get_page_blurb_override('news/'),
    }
    return render(request, "announcements/all_news.html", context)


def json_all_news_json(request):
    context = {
        "restart": get_restart_notice,
        "name": "peter griffin",
        "channel": "fox",
    }
    return JsonResponse(context)


def page_news_by_pk(request, news_pk='1'):
    blurb_page = '/news/detail/' + str(news_pk)
    context = {
        "restart": get_restart_notice,
        "copy_year": datetime.now().year,
        "news_pk": get_news_by_pk(news_pk),
        'release': get_version_json(),
        "title": "News: Full Story",
        # "blurb": "This will show the full story for the article you're reading.",
        # "blurb": get_page_blurb_override('news/'),
        "blurb": get_page_blurb_override(blurb_page),
    }
    return render(request, "announcements/news_by_pk.html", context)


def page_kevin(request):
    context = {
        "restart": get_restart_notice,
        "channel": "fox",
        'release': get_version_json(),
        "title": "Hello Kevin",
        "copy_year": datetime.now().year,
    }
    return render(request, "announcements/helloX.html", context)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
class NewsView(viewsets.ModelViewSet):
    queryset = WhatIsNew.objects.all()
    serializer_class = NewsSerializer


class MainPageBlurbsView(viewsets.ModelViewSet):
    queryset = MainPageBlurbs.objects.all()
    serializer_class = MainPageBlurbsSerializer


class PageBlurbOverridesView(viewsets.ModelViewSet):
    queryset = PageBlurbOverrides.objects.all()
    serializer_class = PageBlurbOverridesSerializer
