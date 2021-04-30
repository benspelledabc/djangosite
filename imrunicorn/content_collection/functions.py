import json
import urllib
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q

from .serializer import BuzzWordOrPhraseSerializer
from .models import Video, PicturesForCarousel, DAndDFifthEditionBook, FantasyGrounds, RandomInsult, Secret, \
    BuzzWordOrPhrase, SensorReadings, ArduinoUnoSketch


def save_buzzword(list_to_save):
    saved_entries = 0
    for word in list_to_save:
        entry = {'word_or_phrase': word}
        try:
            serializer = BuzzWordOrPhraseSerializer(data=entry)
            if serializer.is_valid():
                serializer.save()
                saved_entries += 1
                # print("Saved: {0}".format(word))
        except Exception as ex:
            print(ex)
    return saved_entries


def leach_buzzword():
    html_bytes = ""
    html = ""
    added = 0
    try:
        word_list = []
        url = "https://www.robietherobot.com/buzzword.htm"
        with urllib.request.urlopen('https://www.robietherobot.com/buzzword.htm') as response:
            html_bytes = response.read()
        html = str(html_bytes)
        content_parts = html.split('<td rowspan="5" align="center"><br>')

        for i in range(1, 6):
            item_parts = content_parts[i].split("<p>")
            for item in range(1, len(item_parts) - 1):
                filtered = item_parts[item].split("</p>")
                word_list.append(filtered[0])

        added = save_buzzword(word_list)
    except Exception as ex:
        print("Exception: {0}".format(ex))

    return added


def get_all_buzz_words_or_phrases():
    new_entries = 0
    try:
        new_entries = leach_buzzword()
    except Exception as e:
        print(e)

    result = BuzzWordOrPhrase.objects.all()\
        .order_by('-pk')

    rval = {"result": result, "new_entries": new_entries}
    return rval
    # return result


def get_all_secrets():
    result = Secret.objects.all()\
        .order_by('-pk')
    return result


def get_all_insults():
    result = RandomInsult.objects.all()\
        .order_by('-pk')
    return result


def get_all_fantasy_grounds():
    result = FantasyGrounds.objects.filter()\
        .order_by('-pk', '-file_title', '-file_name')
    return result


def get_dnd5e_by_pk(dnd5e_pk='1'):
    result = DAndDFifthEditionBook.objects.filter(
        Q(pk=dnd5e_pk)
    )
    return result


def get_all_dnd5e():
    result = DAndDFifthEditionBook.objects.filter()\
        .order_by('-pk', '-file_title', '-file_name')
    return result


# sketch functions
def get_sketch_by_pk(sketch_pk='1'):
    result = ArduinoUnoSketch.objects.filter(
        Q(pk=sketch_pk)
    )
    return result


def get_all_sketches():
    result = ArduinoUnoSketch.objects.filter()\
        .order_by('-pk')
    return result


# Video Functions
def get_video_by_pk(video_pk='1'):
    result = Video.objects.filter(
        Q(pk=video_pk)
    )
    return result


def get_all_videos():
    result = Video.objects.filter()\
        .order_by('-pk', '-file_title', '-file_name')
    return result


def get_latest_video():
    result = Video.objects.filter()\
        .order_by('-pk')[0:1]
    return result


# carousel functions
def get_all_pictures_for_carousel():
    result = PicturesForCarousel.objects.filter()\
        .order_by('-pk')
    return result


def get_recent_pictures_for_carousel():
    result = PicturesForCarousel.objects.filter()\
        .order_by('-pk')[0:3]
    return result


# todo: This should take input so we can check several sensors with a single function but i only have one right now
def get_latest_sensor_reading():
    result = SensorReadings.objects.all() \
                 .order_by('-pk')[0:1]
    if result:
        return result[0]
    else:
        return '{"status": "error"}'
    # print("sensor_reading[0].fahrenheit: {0}".format(sensor_reading[0].fahrenheit))
    # result = SensorReadings.objects.all()\
    #     .order_by('-pk')[0:1]
    # return result
