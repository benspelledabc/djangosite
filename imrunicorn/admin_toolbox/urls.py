from django.urls import path
from . import views

app_name = 'admin_toolbox'
urlpatterns = [
    path('', views.no_request_found, name='admin_tools_json_test'),
    # path('test', views.dir_maker, name='admin_tools_test'),
    # path('test-del', views.dir_delete, name='admin_tools_test'),
    path('restart_gunicorn', views.admintool_restart_gunicorn, name='restart_gunicorn'),
    path('restart_nginx', views.admintool_restart_nginx, name='restart_nginx'),
    path('restart_gunicorn_and_nginx', views.admintool_restart_gunicorn_and_nginx, name='restart_gunicorn_and_nginx'),
    path('cancel_all_restarts', views.admintool_cancel_restarts, name='cancel_all_restarts'),
]
