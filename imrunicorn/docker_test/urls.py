from django.urls import path
from . import views

app_name = 'docker_test'
urlpatterns = [
    path('', views.test, name='test'),
]
