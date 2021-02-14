from django.urls import path, include
from . import views

app_name = 'activity_log'
urlpatterns = [
    path('', views.page_blank, name='blank'),
    path('task_list', views.page_task_list, name='task_list'),
    path('tasks_per_user', views.page_tasks_per_user, name='tasks_per_user'),
    path('scoreboard', views.page_scoreboard, name='scoreboard'),
    path('photo_validation', views.page_photo_validation, name='photo_validation'),

]
