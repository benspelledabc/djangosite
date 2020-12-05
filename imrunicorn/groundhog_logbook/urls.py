from django.urls import path, include
from . import views
from .views import HomeView, ChartData, get_data

app_name = 'groundhog_logbook'
urlpatterns = [
    # path('', views.page_all_groundhog_removals, name='all_groundhog_removals'),

    path('by_shooter/', views.page_all_groundhog_removals, name='all_groundhog_removals'),
    path('by_shooter/<int:shooter_pk>', views.page_all_groundhog_removals_by_shooter_pk, name='all_groundhog_removals'),
    path('locations/', views.page_all_groundhog_locations, name='all_groundhog_locations'),
    path('charts/', views.page_charts, name='page_charts'),
    path('removal_scoreboard/', views.page_groundhog_removals_scoreboard, name='groundhog_removal_scoreboard'),
    path('removal_scoreboard_annual/', views.page_groundhog_removals_scoreboard_annual,
         name='groundhog_removal_scoreboard_annual'),
    path('line_charts/', views.page_line_charts, name='page_line_charts'),

    path('', HomeView.as_view(), name="all_groundhog_removals"),

    path("api/data/", get_data, name="api-data"),
    path('api/chart/data/', ChartData.as_view()),




    # path('detail/', views.page_news_by_pk, name='news_by_pk'),
    # path('detail/<int:news_pk>', views.page_news_by_pk, name='news_by_pk'),
]
