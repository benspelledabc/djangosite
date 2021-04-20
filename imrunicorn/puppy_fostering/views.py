from django.shortcuts import render
from announcements.get_news import get_news, get_news_sticky, get_news_by_pk, get_version_json, \
    get_page_blurb_override, get_restart_notice
from imrunicorn.functions import step_hit_count_by_page
from datetime import datetime
from django.shortcuts import render
from .functions import momma_pics, puppies_by_sex, puppies_by_momma, all_puppy_pics


def page_home(request):
    step_hit_count_by_page(request.path)
    # puppies_by_sex_all = puppies_by_sex()
    # puppies_by_sex_male = puppies_by_sex("Male")
    # puppies_by_sex_female = puppies_by_sex("Female")

    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Puppy Fostering",
        "blurb": get_page_blurb_override('puppy_fostering/home/'),
    }
    return render(request, "puppy_fostering/home.html", context)


def page_momma_pics(request):
    step_hit_count_by_page(request.path)
    momma_stuff = momma_pics("All")
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Puppy Fostering: Momma Pics",
        "dataset": momma_stuff,
        "blurb": get_page_blurb_override('puppy_fostering/momma_pics/'),
    }
    return render(request, "puppy_fostering/momma.html", context)


def page_puppy_pics(request):
    step_hit_count_by_page(request.path)
    puppy_pics = all_puppy_pics()
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Puppy Fostering: Puppy Pics",
        "dataset": puppy_pics,
        "blurb": get_page_blurb_override('puppy_fostering/puppy_pics/'),
    }
    return render(request, "puppy_fostering/puppy.html", context)
