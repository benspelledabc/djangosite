from django.urls import path
from . import views

urlpatterns = [
    path('', views.sample, name='home'),
    path('six_steps/', views.page_six_steps_of_firing_a_shot, name='six_steps'),
    path('reading_wind_mirage/', views.page_reading_wind_mirage, name='reading_wind_mirage'),
]
