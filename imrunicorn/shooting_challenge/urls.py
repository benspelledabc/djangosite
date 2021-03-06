from django.urls import path, include
from . import views

app_name = 'shooting_challenge'
urlpatterns = [
    path('', views.page_home, name='home'),
    path('list/', views.page_shooting_challenges_list, name='list'),
    path('list/<int:challenge_pk>', views.page_shooting_challenges_list_by_pk, name='list'),

]
