from django.urls import path, include
from . import views
from rest_framework import routers
from django.views.generic import TemplateView

# similar to object based url building
router = routers.DefaultRouter()
router.register('announcements/what_is_new_random_one', views.WhatIsNewViewRandomOne)
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


# HyperlinkedModelSerializer doesn't like namespace addressing for the 'url' to work
# app_name = 'api'
urlpatterns = [
    # path('DeerWaitListRecipient/', views.DeerWaitListRecipient, name='DeerWaitListRecipient'),
    path('', include(router.urls)),
]
