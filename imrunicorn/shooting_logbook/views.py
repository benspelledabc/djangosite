import datetime as dt
import pytz
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from announcements.get_news import get_news, get_version_json, get_page_blurb_override, get_restart_notice
from imrunicorn.functions import step_hit_count_by_page, get_sunrise_sunset


def page_six_steps_of_firing_a_shot(request):
    step_hit_count_by_page(request.path)
    # http://appleseedshoot.blogspot.com/2008/03/six-steps-of-firing-shot.html

    # any permission check will cache the current set of permissions
    # perm_check = request.user.has_perm('content_collection.view_picturesforcarousel')
    # sun_info = get_sunrise_sunset()

    # # convert sunrise stuff
    # sunrise = sun_info["sunrise"]
    # date_time_str = sunrise
    # date_time_obj = dt.datetime.strptime(date_time_str, '%H:%M:%S %p')
    # # timezone = pytz.timezone('America/New_York')
    # timezone = pytz.timezone('GMT')
    # timezone_date_time_obj = timezone.localize(date_time_obj)
    # target_time_zone = pytz.timezone('America/New_York')
    # target_date_with_timezone = timezone_date_time_obj.astimezone(target_time_zone)
    # sunrise_final = "{0}:{1}".format(target_date_with_timezone.hour, target_date_with_timezone.minute)
    #
    # # convert sunset stuff
    # sunrise = sun_info["sunset"]
    # date_time_str = sunrise
    # date_time_obj = dt.datetime.strptime(date_time_str, '%H:%M:%S %p')
    # # timezone = pytz.timezone('America/New_York')
    # timezone = pytz.timezone('GMT')
    # timezone_date_time_obj = timezone.localize(date_time_obj)
    # target_time_zone = pytz.timezone('America/New_York')
    # target_date_with_timezone = timezone_date_time_obj.astimezone(target_time_zone)
    # sunset_final = "{0}:{1}".format(target_date_with_timezone.hour, target_date_with_timezone.minute)

    context = {
        # 'sunrise': sun_info['sunrise'],
        # 'sunset': sun_info['sunset'],
        "show_lorem": False,
        'release': get_version_json(),
        "title": "6 steps of firing a shot",
        "blurb": get_page_blurb_override('shooting_logbook/six_steps/'),
        "table_data": '',
        "copy_year": datetime.now().year
    }
    return render(request, "shooting_logbook/six_steps_to_firing_a_shot.html", context)


def page_reading_wind_mirage(request):
    step_hit_count_by_page(request.path)
    context = {
        # "restart": get_restart_notice,
        'release': get_version_json(),
        "title": "Reading Wind Mirage",
        # "blurb": "This page is a place holder for what's to come soon.",
        "blurb": get_page_blurb_override('shooting_logbook/reading_wind_mirage/'),
        "copy_year": datetime.now().year
    }
    return render(request, "shooting_logbook/reading_wind_mirage.html", context)


def sample(request):
    step_hit_count_by_page(request.path)
    data = {
        # "restart": get_restart_notice,
        'Query': 'Complete',
        'Result': 'The query completed but this is not an endpoint with data.'
    }
    return JsonResponse(data)
