from django.urls import path
from . import views

app_name = 'farm_invite'
urlpatterns = [
    path('', views.page_farm_invites_view, name='home'),
    path('pending/', views.page_farm_invites_view_hidden_listings, name='view_hidden_listings'),
    path('request_slot/', views.page_invite_listing, name='invite_listing'),
    path('missing_contact_info/', views.page_missing_contact_info, name='missing_contact_info'),
    path('checklist/', views.page_farm_check_list, name='check_list'),
    path('map/', views.page_farm_invites_map_fake, name='map_fake'),
    path('how_do_i_sign_up/', views.page_how_to_sign_up, name='how_do_i_sign_up'),
    path('k98k-is-great-m1-garand-wins-wars/', views.page_farm_invites_map, name='map_secret_sort_of'),

    # path('cash_app/', views.page_cash_app, name='cash_app'),

]
