from django.urls import path, include
from . import views
from .views import ChartDataByTime, ChartDataBySex, ChartDataByMonth, ChartDataByYear, ChartDataByRemover

app_name = 'deer_harvest_logbook'
urlpatterns = [
    path('', views.page_all_harvests, name='all_harvests'),
    path('by_shooter/', views.page_all_harvests, name='all_harvests'),
    path('by_shooter/<int:shooter_pk>', views.page_all_harvests_by_shooter_pk, name='all_harvests'),

    path('point_system/', views.page_point_system, name='point_system'),
    path('point_system/show_points', views.page_point_system_show_points, name='point_system_show_points'),

    path('charts/', views.page_charts_by_time, name='page_charts'),

    path('charts/by_time/', views.page_charts_by_time, name='charts_by_time'),
    path('api/chart/by_time/data/', ChartDataByTime.as_view()),

    path('charts/by_sex/', views.page_charts_by_sex, name='charts_by_sex'),
    path('api/chart/by_sex/data/', ChartDataBySex.as_view()),

    path('charts/by_month/', views.page_charts_by_month, name='charts_by_month'),
    path('api/chart/by_month/data/', ChartDataByMonth.as_view()),

    path('charts/by_year/', views.page_charts_by_year, name='charts_by_year'),
    path('api/chart/by_year/data/', ChartDataByYear.as_view()),

    path('charts/by_remover/', views.page_charts_by_remover, name='charts_by_remover'),
    path('api/chart/by_remover/data/', ChartDataByRemover.as_view()),


    # path('locations/', views.page_all_groundhog_locations, name='all_groundhog_locations'),
    # path('charts/', views.page_charts, name='page_charts'),
    # path('by_shooter/', views.page_all_groundhog_removals, name='all_groundhog_removals'),
    # path('by_shooter/<int:shooter_pk>', views.page_all_groundhog_removals_by_shooter_pk, name='all_groundhog_removals'),
    # path('removal_scoreboard/', views.page_groundhog_removals_scoreboard, name='groundhog_removal_scoreboard'),

    # path('api/chart/', ChartData.as_view()),

    # path('detail/', views.page_news_by_pk, name='news_by_pk'),
    # path('detail/<int:news_pk>', views.page_news_by_pk, name='news_by_pk'),
]
