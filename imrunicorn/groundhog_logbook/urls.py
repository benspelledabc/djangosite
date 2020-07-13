from django.urls import path, include
from . import views
from .views import ChartData

app_name = 'groundhog_logbook'
urlpatterns = [
    path('', views.page_all_groundhog_removals, name='all_groundhog_removals'),
    path('locations/', views.page_all_groundhog_locations, name='all_groundhog_locations'),
    path('charts/', views.page_charts, name='page_charts'),
    path('by_shooter/', views.page_all_groundhog_removals, name='all_groundhog_removals'),
    path('by_shooter/<int:shooter_pk>', views.page_all_groundhog_removals_by_shooter_pk, name='all_groundhog_removals'),
    path('removal_scoreboard/', views.page_groundhog_removals_scoreboard, name='groundhog_removal_scoreboard'),

    path('api/chart/', ChartData.as_view()),


    # path('detail/', views.page_news_by_pk, name='news_by_pk'),
    # path('detail/<int:news_pk>', views.page_news_by_pk, name='news_by_pk'),
]
