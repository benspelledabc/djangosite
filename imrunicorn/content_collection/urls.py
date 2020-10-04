from django.urls import path, include
from . import views

app_name = 'content_collection'
urlpatterns = [
    path('', views.page_blank, name='blank'),
    # path('videos/', views.page_videos, name='videos'),    # disabled because it's slow AF
    path('videos/', views.page_video_list, name='video_list'),
    path('videos/<int:video_pk>', views.page_latest_video_by_pk, name='video_list'),
    path('videos/latest', views.page_latest_video, name='videos_latest'),
]
