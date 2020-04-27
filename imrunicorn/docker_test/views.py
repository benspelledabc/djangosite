from datetime import datetime
from django.conf import settings
from django.db.models import F, FloatField, ExpressionWrapper
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import os
import json

from announcements.get_news import get_news, get_news_sticky, get_version_json, get_page_blurb_override



def test(request):
    context = {
        'body': 'no body to share',
        'header': 'add',
    }
    return JsonResponse(context)
