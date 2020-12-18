from django.urls import path, include
from . import views

app_name = 'call_of_the_wild'
urlpatterns = [
    path('', views.page_blank, name='blank'),
    path('need_zone_times', views.page_need_zone_times, name='page_need_zone_times'),

]
