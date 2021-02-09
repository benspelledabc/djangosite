from django.shortcuts import render
from announcements.get_news import get_version_json, get_page_blurb_override
from imrunicorn.functions import step_hit_count_by_page
from datetime import datetime
from django.shortcuts import render
from imrunicorn.decorators import allowed_groups


@allowed_groups(allowed_groupname_list=['activity_log_viewer', 'activity_log_tasker'])
def page_blank(request):
    step_hit_count_by_page(request.path)
    context = {
        "copy_year": datetime.now().year,
        'release': get_version_json(),
        "title": "Activity Log: Blank",
        "blurb": get_page_blurb_override('activity_log/blank/'),
    }
    return render(request, "activity_log/blank.html", context)
