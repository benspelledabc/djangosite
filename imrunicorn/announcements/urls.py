from django.urls import path
from . import views


urlpatterns = [
    path('', views.page_all_news, name='all_news'),
]
