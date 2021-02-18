from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from announcements.get_news import get_version_json, get_page_blurb_override, get_page_secret
from groundhog_logbook.functions import groundhog_removal_scoreboard
from imrunicorn.functions import step_hit_count_by_page
from datetime import datetime
from django.shortcuts import render
from imrunicorn.decorators import allowed_groups
from .functions import activity_list, activity_scoreboard, activity_tasks_per_user, \
    activity_photo_validation, activity_scoreboard_by_user


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
        "blurb": get_page_blurb_override('activity_log/task_list/'),
        "secret": get_page_secret('activity_log/task_list/'),
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
        "blurb": get_page_blurb_override('activity_log/tasks_per_user/'),
        "data": data,
    }
    return render(request, "activity_log/tasks_per_user.html", context)


@allowed_groups(allowed_groupname_list=['activity_log_viewer', 'activity_log_tasker'])
def page_current_points(request):
    step_hit_count_by_page(request.path)
    data = activity_tasks_per_user()
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Activity Log: Current Points",
        "blurb": get_page_blurb_override('activity_log/current_points/'),
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


def page_scoreboard_by_user(request):
    step_hit_count_by_page(request.path)

    context = {
        "graph_api_node": '/activity_log/api/chart/scoreboard/by_user/data/',
        "graph_header": "# points (By User)",
        "graph_message": "Running total (no resets)",
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Scoreboard Line Charts",
        "blurb": get_page_blurb_override('activity_log/charts/scoreboard/'),
    }
    return render(request, "activity_log/activity_log_graphic_generic.html", context)


class ChartDataScoreByUser(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        by_hour = activity_scoreboard_by_user()
        labels = []
        default_items = []

        for item in by_hour:
            if item['actor__userprofile__preferred_display_name']:
                labels.append(item['actor__userprofile__preferred_display_name'])
            else:
                labels.append(item['actor__username'])

        for item in by_hour:
            default_items.append(item['points'])

        data = {
            "labels": labels,
            "default": default_items,
            "endpoint": "/activity_log/api/chart/scoreboard/by_user/data/",
            "graph_title": "# of Groundhog Removals (By Temperature)"
        }
        return Response(data)
