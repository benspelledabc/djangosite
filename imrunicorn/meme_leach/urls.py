from django.urls import path
from . import views


app_name = 'meme_leach'
urlpatterns = [
    path('', views.page_sfw_meme_list, name='home'),
    path('sfw-list/', views.page_sfw_meme_list, name='sfw_meme_list'),
    path('nsfw-list/', views.page_nsfw_meme_list, name='nsfw_meme_list'),
    path('fetch/', views.page_meme, name='subreddit'),
    path('fetch/<str:subreddit>/', views.page_meme_by_subreddit, name='subreddit'),
]

