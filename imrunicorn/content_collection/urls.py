from django.urls import path, include
from . import views

app_name = 'content_collection'
urlpatterns = [
    path('', views.page_home, name='home'),

    path('videos/', views.page_video_list, name='video_list'),
    path('videos/<int:video_pk>', views.page_latest_video_by_pk, name='video_list'),

    path('videos/latest', views.page_latest_video, name='videos_latest'),

    path('carousel', views.page_carousel, name='carousel'),
    path('carousel/recent', views.page_carousel_recent, name='carousel_recent'),

    path('dnd5e', views.page_dnd5e_list, name='dnd5e_list'),
    path('fantasy_grounds', views.page_fantasy_grounds_list, name='fantasy_grounds_list'),

    path('insult', views.leach_insult, name='insult'),
    path('insult_list_all', views.insult_list_all, name='insult_list_all'),

    path('secrets_list_all', views.secrets_list_all, name='secrets_list_all'),

    # path('dnd5e/<int:dnd5e_pk>', views.page_dnd5e_list_by_pk, name='dnd5e_list'),

]
