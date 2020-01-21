from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_farm_invites_view, name='farm_invites_home'),
    path('request_slot/', views.page_invite_listing, name='invite_listing'),
    path('missing_contact_info/', views.page_missing_contact_info, name='missing_contact_info'),
    path('checklist/', views.page_farm_check_list, name='farm_check_list'),
    path('map/', views.page_farm_invites_map_fake, name='farm_invites_map_fake'),
    path('map-of-the-farm-k98k-is-great-m1-garand-wins-wars/', views.page_farm_invites_map, name='farm_invites_map_secret_sort_of'),
    # path('map-of-the-farm-President-Trump-Appleseed-k98k-is-great-22lr-is-pitd/', views.page_farm_invites_map, name='farm_invites_map_secret_sort_of'),
    # path('', views.page_loads, name='home'),
    # path('loads/', views.page_loads, name='loads'),

]

