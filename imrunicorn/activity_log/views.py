from django.shortcuts import render
from announcements.get_news import get_version_json, get_page_blurb_override
from imrunicorn.functions import step_hit_count_by_page
from datetime import datetime
from django.shortcuts import render
from imrunicorn.decorators import allowed_groups
from .functions import activity_list, activity_scoreboard, activity_tasks_per_user, activity_photo_validation


@allowed_groups(allowed_groupname_list=['activity_log_viewer', 'activity_log_tasker'])
def page_blank(request):
    step_hit_count_by_page(request.path)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Activity Log: home",
        "blurb": get_page_blurb_override('activity_log/home/'),
    }
    return render(request, "activity_log/home.html", context)


@allowed_groups(allowed_groupname_list=['activity_log_viewer', 'activity_log_tasker'])
def page_task_list(request):
    step_hit_count_by_page(request.path)
    data = activity_list()
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Activity Log: Task List",
        "blurb": get_page_blurb_override('activity_log/home/'),
        "data": data,
    }
    return render(request, "activity_log/activity_list.html", context)


@allowed_groups(allowed_groupname_list=['activity_log_viewer', 'activity_log_tasker'])
def page_tasks_per_user(request):
    step_hit_count_by_page(request.path)
    data = activity_tasks_per_user()
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Activity Log: Tasks Per User",
        "blurb": get_page_blurb_override('activity_log/home/'),
        "data": data,
    }
    return render(request, "activity_log/tasks_per_user.html", context)


@allowed_groups(allowed_groupname_list=['activity_log_viewer', 'activity_log_tasker'])
def page_photo_validation(request):
    step_hit_count_by_page(request.path)
    data = activity_photo_validation()
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Activity Log: Photo Validation",
        "blurb": get_page_blurb_override('activity_log/photo_validation/'),
        "data": data,
    }
    return render(request, "activity_log/photo_validation.html", context)


@allowed_groups(allowed_groupname_list=['activity_log_viewer', 'activity_log_tasker'])
def page_scoreboard(request):
    step_hit_count_by_page(request.path)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Activity Log: Scoreboard",
        "blurb": get_page_blurb_override('activity_log/home/'),
    }
    return render(request, "activity_log/activity_log_graphic_generic.html", context)
