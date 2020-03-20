from django.urls import path, include
from . import views

app_name = 'groundhog_logbook'
urlpatterns = [
    path('', views.page_all_groundhog_removals, name='all_groundhog_removals'),
    path('locations/', views.page_all_groundhog_locations, name='all_groundhog_locations'),
    path('by_shooter/', views.page_all_groundhog_removals, name='all_groundhog_removals'),
    path('by_shooter/<int:shooter_pk>', views.page_all_groundhog_removals_by_shooter_pk, name='all_groundhog_removals'),

    # path('detail/', views.page_news_by_pk, name='news_by_pk'),
    # path('detail/<int:news_pk>', views.page_news_by_pk, name='news_by_pk'),
]
