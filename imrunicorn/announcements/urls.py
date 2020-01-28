from django.urls import path, include
from . import views
from rest_framework import routers

# similar to object based url building
router = routers.DefaultRouter()
router.register('news_api', views.NewsView)
# router.register('courses', views.CourseView)

urlpatterns = [
    path('', views.page_all_news, name='all_news'),
    path('', include(router.urls)),
    # path('all_news_json/', views.json_all_news_json, name='all_news_json'),
]
