from django.urls import path, include
from . import views

app_name = 'content_collection'
urlpatterns = [
    path('', views.page_blank, name='blank'),
]
