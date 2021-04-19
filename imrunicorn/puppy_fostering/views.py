from django.shortcuts import render
from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, \
    get_page_blurb_override, get_restart_notice
from imrunicorn.functions import step_hit_count_by_page
from datetime import datetime
from django.shortcuts import render


def page_home(request):
    step_hit_count_by_page(request.path)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Puppy Fostering",
        "blurb": get_page_blurb_override('puppy_fostering/home/'),
    }
    return render(request, "puppy_fostering/home.html", context)


def page_momma_pics(request):
    step_hit_count_by_page(request.path)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Puppy Fostering: Momma Pics",
        "blurb": get_page_blurb_override('puppy_fostering/home/'),
    }
    return render(request, "puppy_fostering/home.html", context)


def page_puppy_pics(request):
    step_hit_count_by_page(request.path)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Puppy Fostering: Puppy Pics",
        "blurb": get_page_blurb_override('puppy_fostering/home/'),
    }
    return render(request, "puppy_fostering/home.html", context)
