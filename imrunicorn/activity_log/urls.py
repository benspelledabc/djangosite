from django.urls import path, include
# from views import ChartDataScoreByUser
from . import views
from .views import ChartDataScoreByUser


app_name = 'activity_log'
urlpatterns = [
    path('', views.page_blank, name='blank'),
    path('task_list', views.page_task_list, name='task_list'),
    path('tasks_per_user', views.page_tasks_per_user, name='tasks_per_user'),
    path('current_points', views.page_current_points, name='current_points'),

    path('photo_validation', views.page_photo_validation, name='photo_validation'),

    path('charts/scoreboard/', views.page_scoreboard_by_user, name='scoreboard_by_user'),
    path('api/chart/scoreboard/by_user/data/', ChartDataScoreByUser.as_view()),

]
