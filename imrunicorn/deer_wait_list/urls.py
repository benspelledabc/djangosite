from django.urls import path, include
from . import views

app_name = 'deer_wait_list'
urlpatterns = [
    path('', views.page_blank, name='blank'),
    path('info/', views.page_info, name='info'),
    path('list/view/', views.page_list_view, name='list_view'),
]
