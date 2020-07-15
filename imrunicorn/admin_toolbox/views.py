import json
import os
from datetime import datetime
from django.conf import settings
from django.db.models import Q
from django.db.models import F, ExpressionWrapper
from django.http import JsonResponse
from django.shortcuts import render
from model_utils.models import now


# Create your views here.
def json_test(request):
    context = {
        'body': 'no body to share',
        'header': 'farm invites view',
    }
    return JsonResponse(context)
