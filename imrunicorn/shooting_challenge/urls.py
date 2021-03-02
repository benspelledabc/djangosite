from django.urls import path, include
from . import views

app_name = 'shooting_challenge'
urlpatterns = [
    path('', views.page_home, name='home'),
    path('2021_520y_egg_challenge', views.page_shooting_challenges_list, name='list'),

]
