from django.urls import path, include
from . import views
from content_collection import views as c_views
# from meme_leach import views as meme_leach_views
from rest_framework import routers
from django.views.generic import TemplateView
# from api.views import ChartData as GroundHogChartData
from groundhog_logbook.views import ChartDataBySex
# from api.views import ChartDataTest
from .views import ActivityLogViewSet

# similar to object based url building
router = routers.DefaultRouter()
# router.get_api_root_view().cls.__name__ = "BenSpelledABC: API"
# router.get_api_root_view().cls.__doc__ = "Becoming the backbone to wonderland."

router.register('activity_log/activity', views.ActivityViewSet)
router.register('activity_log/activity_log', views.ActivityLogViewSet)
router.register('activity_log/activity_photo_validation', views.ActivityPhotoValidationViewSet)

router.register('announcements/what_is_new', views.WhatIsNewView)
router.register('announcements/main_page_blurbs', views.MainPageBlurbsView)
router.register('announcements/page_blurb_overrides', views.PageBlurbOverridesView)

router.register('content_collection/insults', views.ContentCollectionInsultsViewSet)

router.register('deer_wait_list/Recipient', views.DeerWaitListRecipient)
router.register('deer_wait_list/MeatCut', views.DeerWaitListMeatCut)
router.register('deer_wait_list/Flavor', views.DeerWaitListFlavor)
router.register('deer_wait_list/RequestedOrder', views.DeerWaitListRequestedOrder)

router.register('loaddata/Owner', views.Owner)
router.register('loaddata/Caliber', views.LoadDataCaliber)
router.register('loaddata/Firearm', views.LoadDataFirearm)
router.register('loaddata/Powder', views.LoadDataPowder)
router.register('loaddata/Projectile', views.LoadDataProjectile)
router.register('loaddata/Brass', views.LoadDataBrass)
router.register('loaddata/Primer', views.LoadDataPrimer)
router.register('loaddata/HandLoad', views.LoadDataHandLoad)
router.register('loaddata/EstimatedDope', views.LoadDataEstimatedDope)

router.register('groundhog_logbook/Location', views.LocationView)
router.register('groundhog_logbook/RemovalsByLocation', views.RemovalsByLocationView)
# router.register('groundhog_logbook/chart/data/test', ChartDataTest.as_view(), basename=ChartDataTest)

router.register('deer_harvest_logbook/Harvests', views.HarvestsView)
router.register('deer_harvest_logbook/HarvestsPhotos', views.HarvestsPhotosView)

router.register('shooting_challenge/ChallengeEvent', views.ChallengeEventViewSet)
router.register('shooting_challenge/ChallengePhoto', views.ChallengePhotoViewSet)

router.register('accounts', views.Accounts)

router.register('meme_leach', views.MemeLeachViewSet)
# router.register('meme_leach/<str:subreddit>', views.MemeLeachViewSet.random_meme_by_subreddit_name)

# router.register('sensor_reading', c_views.sensor_readings)

# /api/docker/hook
# router.register('docker_hub_hook', views.docker_hub_webhook)


# HyperlinkedModelSerializer doesn't like namespace addressing for the 'url' to work
# app_name = 'api'
urlpatterns = [
    # path('DeerWaitListRecipient/', views.DeerWaitListRecipient, name='DeerWaitListRecipient'),
    # path("activity_log", ActivityLogViewSet.as_view(), name='activity_log'),
    path('', include(router.urls)),
    path('docker_hub_hook/', views.docker_hub_webhook, name='docker_hub_webhook'),
    path('sensor_reading/', c_views.sensor_readings, name='sensor_readings'),

    path('meme_leach/<str:subreddit>', views.random_meme_by_subreddit),
]
