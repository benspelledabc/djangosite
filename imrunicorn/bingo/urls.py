from django.urls import path, include
from . import views

app_name = 'bingo'
urlpatterns = [
    path('', views.page_home, name='home'),
    path('buzz_word', views.page_buzz_words_or_phrases, name='buzz_words_or_phrases'),

]
