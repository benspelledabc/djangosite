from django.urls import path, include
from . import views
from .views import ChartDataBySex, ChartDataByTime, ChartDataByMonth, ChartDataByCloudLevel, ChartDataByTemperature, \
    ChartDataByRemover, ChartDataByYear, ChartDataByCaliber, ChartDataByDistance
# from api.views import ChartData as GroundHogChartData


app_name = 'groundhog_logbook'
urlpatterns = [
    path('by_shooter/', views.page_all_groundhog_removals, name='all_groundhog_removals'),
    path('by_shooter/<int:shooter_pk>', views.page_all_groundhog_removals_by_shooter_pk, name='all_groundhog_removals'),

    path('', views.page_all_groundhog_removals, name='all_groundhog_removals_base'),
    path('locations/', views.page_all_groundhog_locations, name='all_groundhog_locations'),
    path('charts/', views.page_charts, name='page_charts'),
    path('removal_scoreboard/', views.page_groundhog_removals_scoreboard, name='groundhog_removal_scoreboard'),
    path('removal_scoreboard_annual/', views.page_groundhog_removals_scoreboard_annual,
         name='groundhog_removal_scoreboard_annual'),

    # charts by sex
    path('charts/by_sex/', views.page_charts_by_sex, name='charts_by_sex'),
    path('api/chart/by_sex/data/', ChartDataBySex.as_view()),

    path('charts/by_time/', views.page_charts_by_time, name='charts_by_time'),
    path('api/chart/by_time/data/', ChartDataByTime.as_view()),

    path('charts/by_month/', views.page_charts_by_month, name='charts_by_month'),
    path('api/chart/by_month/data/', ChartDataByMonth.as_view()),

    path('charts/by_year/', views.page_charts_by_year, name='charts_by_year'),
    path('api/chart/by_year/data/', ChartDataByYear.as_view()),

    path('charts/by_cloud_level/', views.page_charts_by_cloud_level, name='charts_by_cloud_level'),
    path('api/chart/by_cloud_level/data/', ChartDataByCloudLevel.as_view()),

    path('charts/by_temperature/', views.page_charts_by_temperature, name='charts_by_temperature'),
    path('api/chart/by_temperature/data/', ChartDataByTemperature.as_view()),

    path('charts/by_remover/', views.page_charts_by_remover, name='charts_by_remover'),
    path('api/chart/by_remover/data/', ChartDataByRemover.as_view()),

    path('charts/by_caliber/', views.page_charts_by_caliber, name='charts_by_caliber'),
    path('api/chart/by_caliber/data/', ChartDataByCaliber.as_view()),

    path('charts/by_distance/', views.page_charts_by_distance, name='charts_by_distance'),
    path('api/chart/by_distance/data/', ChartDataByDistance.as_view()),

]
