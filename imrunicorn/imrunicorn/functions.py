# import json
# from datetime import datetime
# from django.conf import settings
# from django.contrib.auth.models import User
import requests
import os
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from .models import PageCounter
from django.contrib.auth.models import User
import logging
from decouple import config, AutoConfig

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = AutoConfig(search_path=BASE_DIR)

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)


def get_weather(request, lat='39.620863010825495', lon='-77.02896921045372'):
    context = {
        "completed": False,
        "message": "pre-query",
        "lat": lat,
        "lon": lon,
    }

    try:
        # open_weather_map_api_key = "c01389f69a2da5f476498c2bf09c37ed"
        open_weather_map_api_key = config('OPEN_WEATHER_MAP_API_KEY', default='c01389f69a2da5f476498c2bf09c37ed')
        url = 'http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&units=imperial&appid={2}'.format(
            lat, lon, open_weather_map_api_key)
        r = requests.get(url).json()
        # weather_icon_url = 'http://openweathermap.org/img/wn/{0}@2x.png'.format(r['weather'][0]['icon'])
        weather_icon_url = 'http://openweathermap.org/img/wn/{0}.png'.format(r['weather'][0]['icon'])
        print(r)

        '''
        clear sky
        few clouds 
        scattered clouds 
        broken clouds 
        shower rain 
        rain
        thunderstorm 
        snow
        mist
        '''

        context = {
            'lat': lat,
            'lon': lon,
            'temperature': r['main']['temp'],
            'feels_like': r['main']['feels_like'],
            'wind_speed': r['wind']['speed'],
            'wind_dir': r['wind']['deg'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'weather_icon_url': weather_icon_url,
            'full_response': r,
        }
    except Exception as e:
        print(e)

    return context


# create an entry or step it up if there is one.
def step_hit_count_by_page(input_page_name='/'):
    result = PageCounter.objects.filter(
        Q(page_name=input_page_name)
    )[0:1]
    if not result:
        result = PageCounter.objects.create(page_name=input_page_name, page_hit_count=1)
    else:
        result[0].page_hit_count = result[0].page_hit_count + 1
        result[0].page_name = input_page_name
        result[0].save()

    return result


def email_user(email_name, email_subject, email_body_lines):
    try:
        email_body = ""
        for line in email_body_lines:
            email_body = email_body + "{0}\n\r".format(line)

        email_from = settings.EMAIL_HOST_USER
        subject = email_subject
        message = "****************************************************************************************\n"
        message = message + "* This is an Automated email, but I do monitor the inbox. Feel free to reply. \n"
        message = message + "*                                                                             \n"
        message = message + "*                                                        -- BenSpelledABC.me  \n"
        message = message + "****************************************************************************************\n"
        message = "%s\n\r%s" % (message, email_body)
        recipient_list = [email_name]
        logger.warning("Sent email to {0} as {1} with password {2}"
                       .format(email_name, email_from, settings.EMAIL_HOST_PASSWORD))

        result = send_mail(subject, message, email_from, recipient_list)
    except Exception as e:
        print("Exception: {0}".format(e))
        logger.error("Failed to send email to {0}".format(email_name))
        return False

    return True
