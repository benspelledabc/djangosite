from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_farm_invites_view, name='farm_invites_home'),
    # path('', views.page_loads, name='home'),
    # path('loads/', views.page_loads, name='loads'),
]

