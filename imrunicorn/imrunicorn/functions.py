# import json
# from datetime import datetime
# from django.conf import settings
# from django.contrib.auth.models import User
import datetime
import time

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


def get_sunrise_sunset(lat='39.6212340', lng='-77.0276600'):
    # https://api.sunrise-sunset.org/json?lat=39.6212340&lng=-77.0276600
    # end_point = "https://api.sunrise-sunset.org/json?lat={0}&lng={1}&formatted=0".format(lat, lng)
    end_point = "https://api.sunrise-sunset.org/json?lat={0}&lng={1}".format(lat, lng)
    response = requests.get(end_point)
    result = response.json()
    return result


# def get_weather(request, lat='36.998944', lon='-109.045298'):  # 4 corners usa for testing
def get_weather(request, lat='39.620863010825495', lon='-77.02896921045372'):
    context = {
        'lat': '39.620863010825495',
        'lon': '-77.02896921045372',
        'temperature': '115',
        'feels_like': '114',
        'wind_speed': '223',
        'wind_dir': '14',
        'wind_dir_word': 'North',
        'description': 'pre-fetch values',
        'icon': '007',
        'weather_icon_url': 'https://google.com',
        'full_response': 'empty placeholder',
    }

    try:
        # open_weather_map_api_key = "c01389f69a2da5f476498c2bf09c37ed"
        open_weather_map_api_key = config('OPEN_WEATHER_MAP_API_KEY', default='c01389f69a2da5f476498c2bf09c37ed')
        url = 'http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&units=imperial&appid={2}'.format(
            lat, lon, open_weather_map_api_key)
        r = requests.get(url).json()
        # print(r)
        # weather_icon_url = 'http://openweathermap.org/img/wn/{0}@2x.png'.format(r['weather'][0]['icon'])
        weather_icon_url = 'http://openweathermap.org/img/wn/{0}.png'.format(r['weather'][0]['icon'])
        # print(r)

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

        # figure out the direction
        '''
        0 - 15 = n
        16 - 30 = nne
        31 - 60 = ne
        61 - 75 = ene
        76 - 105 = e
        106 - 120 = ese
        121 - 150 = se
        151 - 165 = sse
        166 - 195 = s
        196 - 210 = ssw
        211 - 240 = sw
        241 - 255 = wsw
        256 - 285 = w
        286 - 300 = wnw
        301 - 330 = nw
        331 - 345 = nnw
        346 - 365 = n
        '''

        # if 10000 <= number <= 30000:
        wind_dir_deg = r['wind']['deg']
        wind_dir_word = "Z"
        # print("wind direction: {0}".format(wind_dir_deg))
        if 0 <= wind_dir_deg <= 15:
            wind_dir_word = "North"
        elif 16 <= wind_dir_deg <= 30:
            wind_dir_word = "North-North-East"
        elif 31 <= wind_dir_deg <= 60:
            wind_dir_word = "North-East"
        elif 61 <= wind_dir_deg <= 75:
            wind_dir_word = "East-North-East"
        elif 76 <= wind_dir_deg <= 105:
            wind_dir_word = "East"
        elif 106 <= wind_dir_deg <= 120:
            wind_dir_word = "East-South-East"
        elif 121 <= wind_dir_deg <= 150:
            wind_dir_word = "South-East"
        elif 151 <= wind_dir_deg <= 165:
            wind_dir_word = "South-South-East"
        elif 166 <= wind_dir_deg <= 195:
            wind_dir_word = "South"
        elif 196 <= wind_dir_deg <= 210:
            wind_dir_word = "South-South-West"
        elif 211 <= wind_dir_deg <= 240:
            wind_dir_word = "South-West"
        elif 241 <= wind_dir_deg <= 255:
            wind_dir_word = "West-South-West"
        elif 256 <= wind_dir_deg <= 285:
            wind_dir_word = "West"
        elif 286 <= wind_dir_deg <= 300:
            wind_dir_word = "West-North-West"
        elif 301 <= wind_dir_deg <= 330:
            wind_dir_word = "North-West"
        elif 331 <= wind_dir_deg <= 345:
            wind_dir_word = "North-North-West"
        elif 346 <= wind_dir_deg <= 365:
            wind_dir_word = "North"
        else:
            wind_dir_word = "Divide By Zero"

        # convert that time for readability!
        sunrise = r['sys']['sunrise']
        sunrise = time.ctime(sunrise)
        sunrise = sunrise.split(' ')

        sunset = r['sys']['sunset']
        sunset = time.ctime(sunset)
        sunset = sunset.split(' ')
        
        wind_speed_gust = 0
        try:
            wind_speed_gust = r['wind']['gust']
        except Exception as e:
            wind_speed_gust = 0
            print("Weather json output doesn't have GUST info this time. ({0})".format(e))

        context = {
            'lat': lat,
            'lon': lon,
            'sunrise': sunrise[3],
            'sunset': sunset[3],
            'temperature': r['main']['temp'],
            'feels_like': r['main']['feels_like'],
            'pressure': r['main']['pressure'],
            'humidity': r['main']['humidity'],
            'wind_speed': r['wind']['speed'],
            'wind_speed_gust': wind_speed_gust,     # gust isn't always in the dataset!
            'wind_dir': r['wind']['deg'],
            'wind_dir_word': wind_dir_word,
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'weather_icon_url': weather_icon_url,
            'full_response': r,
        }
    except Exception as e:
        print("Error fetching weather. Element might not exist. {0}", e)

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
