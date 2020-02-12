from django.urls import path
from . import views

app_name = 'farm_invite'
urlpatterns = [
    path('', views.page_farm_invites_view, name='farm_invites_home'),
    path('pending/', views.page_farm_invites_view_hidden_listings, name='farm_invites_view_hidden_listings'),
    path('request_slot/', views.page_invite_listing, name='invite_listing'),
    path('missing_contact_info/', views.page_missing_contact_info, name='missing_contact_info'),
    path('checklist/', views.page_farm_check_list, name='farm_check_list'),
    path('map/', views.page_farm_invites_map_fake, name='farm_invites_map_fake'),
    path('map-of-the-farm-k98k-is-great-m1-garand-wins-wars/', views.page_farm_invites_map, name='farm_invites_map_secret_sort_of'),
]
