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
from announcements.get_news import get_news, get_version_json
from django.shortcuts import render
from rest_framework import viewsets

from .models import WhatIsNew
from .serializer import NewsSerializer

import logging
# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)


#
# logging.config.dictConfig({
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'console': {
#             'format': '%(name)-12s %(levelname)-8s %(message)s'
#         },
#         'file': {
#             'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
#         }
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'console'
#         },
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'formatter': 'file',
#             'filename': '/tmp/debug2.log'
#         }
#     },
#     'loggers': {
#         '': {
#             'level': 'DEBUG',
#             'handlers': ['console', 'file']
#         }
#     }
# })

# Create your views here.
def page_all_news(request):
    logger.info("This is not getting logged...")
    context = {
        "copy_year": datetime.now().year,
        "all_news": get_news,
        'release': get_version_json(),
        "title": "All the news",
        "news_overview": "I've decided to make a blog of sorts. It's super light for speed and readability on "
                         "cellphones. I'll expand functionality later but for now this is just a listing of the "
                         "'Announcements' published.",
    }
    return render(request, "announcements/all_news.html", context)


def json_all_news_json(request):
    context = {
        "name": "peter griffin",
        "channel": "fox",
    }
    return JsonResponse(context)


def page_kevin(request):
    context = {
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
