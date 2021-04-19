from django.urls import path, include
from . import views

app_name = 'puppy_fostering'
urlpatterns = [
    path('', views.page_home, name='home'),
    path('momma_pics/', views.page_momma_pics, name='momma_pics'),
    path('puppy_pics/', views.page_puppy_pics, name='puppy_pics'),

]
