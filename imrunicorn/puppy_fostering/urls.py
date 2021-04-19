from django.urls import path, include
from . import views

app_name = 'puppy_fostering'
urlpatterns = [
    path('', views.page_home, name='home'),

]
