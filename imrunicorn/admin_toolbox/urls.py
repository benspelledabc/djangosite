from django.urls import path
from . import views

app_name = 'admin_toolbox'
urlpatterns = [
    path('', views.json_test, name='admin_tools_json_test'),
]
