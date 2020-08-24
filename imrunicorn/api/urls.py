from django.urls import path, include
from . import views
from rest_framework import routers
from django.views.generic import TemplateView

# similar to object based url building
router = routers.DefaultRouter()
router.register('what_is_new', views.NewsView)
router.register('main_page_blurbs', views.MainPageBlurbsView)
router.register('page_blurb_overrides', views.PageBlurbOverridesView)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]
