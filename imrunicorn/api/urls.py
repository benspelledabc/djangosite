from django.urls import path, include
from . import views
from rest_framework import routers
from django.views.generic import TemplateView
# from api.views import ChartData as GroundHogChartData
from groundhog_logbook.views import ChartDataBySex
# from api.views import ChartDataTest
from .views import ActivityLogViewSet

# similar to object based url building
router = routers.DefaultRouter()

router.register('activity_log/activity', views.ActivityViewSet)
router.register('activity_log/activity_log', views.ActivityLogViewSet)
router.register('activity_log/activity_photo_validation', views.ActivityPhotoValidationViewSet)

router.register('announcements/what_is_new', views.WhatIsNewView)


router.register('announcements/main_page_blurbs', views.MainPageBlurbsView)
router.register('announcements/page_blurb_overrides', views.PageBlurbOverridesView)

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


# HyperlinkedModelSerializer doesn't like namespace addressing for the 'url' to work
# app_name = 'api'
urlpatterns = [
    # path('DeerWaitListRecipient/', views.DeerWaitListRecipient, name='DeerWaitListRecipient'),
    # path("activity_log", ActivityLogViewSet.as_view(), name='activity_log'),
    path('', include(router.urls)),
]
