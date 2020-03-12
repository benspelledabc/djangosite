from django.urls import path, include
from . import views
from rest_framework import routers

# similar to object based url building
router = routers.DefaultRouter()
router.register('news_api', views.NewsView)
# router.register('courses', views.CourseView)

# app_name = 'announcements'
urlpatterns = [
    path('', views.page_all_news, name='all_news'),
    path('', include(router.urls)),

    path('<int:news_pk>', views.page_news_by_pk, name='page_news_by_pk'),
]
