from django.urls import path
from . import views

app_name = 'admin_toolbox'
urlpatterns = [
    path('', views.json_test, name='admin_tools_json_test'),
    path('restart_gunicorn', views.json_test, name='admin_tools_json_test'),
    path('restart_nginx', views.json_test, name='admin_tools_json_test'),
    path('restart_gunicorn_and_nginx', views.json_test, name='admin_tools_json_test'),
    path('cancel_all_restarts', views.json_test, name='admin_tools_json_test'),
]
