import json
import urllib
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q

from content_collection.serializer import BuzzWordOrPhraseSerializer
from content_collection.models import BuzzWordOrPhrase


def get_bingo_card_buzz_words():
    # get 25 words for BINGO card
    #
    result = BuzzWordOrPhrase.objects.filter()\
        .order_by('?')[0:25]
    return result
