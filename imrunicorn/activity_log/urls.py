from django.urls import path, include
from . import views

app_name = 'activity_log'
urlpatterns = [
    path('', views.page_blank, name='blank'),

]
