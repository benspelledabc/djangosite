from django.urls import path
from . import views

app_name = 'status_watcher'
urlpatterns = [
    path('', views.page_view_watches, name='home'),
    path('view_watches', views.page_view_watches, name='view_watches'),
    path('view_watches/reset', views.page_view_watches_reset, name='view_watches_reset'),

    # path('six_steps/', views.page_six_steps_of_firing_a_shot, name='six_steps'),
    # path('reading_wind_mirage/', views.page_reading_wind_mirage, name='reading_wind_mirage'),
]
