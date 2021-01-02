# import json
# from datetime import datetime
# from django.conf import settings
# from django.contrib.auth.models import User
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
import logging
from .models import PackingListItem, PackingList

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)


def get_packing_list(list_size=1):
    result = PackingList.objects.all().order_by('-List_Date')[:list_size]

    return result

