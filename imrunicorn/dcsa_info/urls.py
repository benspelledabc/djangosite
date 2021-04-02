from django.urls import path, include
from . import views
from .views import ChartDataByMonth, ChartDataByYear

app_name = 'dcsa_info'
urlpatterns = [
    path('', views.page_blank, name='blank'),
    path('info/', views.page_info, name='info'),
    path('success_examples/', views.page_success_examples, name='success_examples'),
    path('all_examples/', views.page_all_examples, name='all_examples'),
    path('coming_soon/', views.page_coming_soon, name='coming_soon'),

    path('charts/by_year/', views.page_charts_by_year, name='charts_by_year'),
    path('api/chart/by_year/data/', ChartDataByYear.as_view()),

    path('charts/by_month/', views.page_charts_by_month, name='charts_by_month'),
    path('api/chart/by_month/data/', ChartDataByMonth.as_view()),

]
