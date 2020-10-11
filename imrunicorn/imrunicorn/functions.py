import json
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q
from .models import PageCounter


# create an entry or step it up if there is one.
def step_hit_count_by_page(input_page_name='/'):
    result = PageCounter.objects.filter(
        Q(page_name=input_page_name)
    )[0:1]
    # print(result)
    if not result:
        result = PageCounter.objects.create(page_name=input_page_name, page_hit_count=1)
    else:
        result[0].page_hit_count = result[0].page_hit_count + 1
        result[0].page_name = input_page_name
        result[0].save()

    return result

#
# def get_video_by_pk(video_pk='1'):
#     result = Video.objects.filter(
#         Q(pk=video_pk)
#     )
#
#     return result
#
#
# def get_all_videos():
#     result = Video.objects.filter()\
#         .order_by('-pk', '-file_title', '-file_name')
#     return result
#
#
# def get_latest_video():
#     result = Video.objects.filter()\
#         .order_by('-pk')[0:1]
#     return result
