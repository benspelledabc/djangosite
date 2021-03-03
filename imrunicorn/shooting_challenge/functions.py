# import json
# from datetime import datetime
# from django.conf import settings
# from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
import logging
from .models import ChallengeEvent, ChallengePhoto

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)


def get_shooting_challenges(request):
    result = ChallengeEvent.objects.filter() \
        .order_by('-challenge_date', '-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(result, 3)  # records per pagination

    try:
        result_set = paginator.page(page)
    except PageNotAnInteger:
        result_set = paginator.page(1)
    except EmptyPage:
        result_set = paginator.page(paginator.num_pages)

    return result_set


def get_shooting_challenges_by_id(challenge_pk='1'):
    result = ChallengeEvent.objects.filter(id=challenge_pk)
    # print(result)
    return result
