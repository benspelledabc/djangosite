from django.urls import path
from . import views

# router = routers.DefaultRouter()
# router.register('roll', views.RollView)
# router.register('student', views.StudentView)
# router.register('courses', views.CourseView)

app_name = 'load_data'
urlpatterns = [
    path('', views.page_loads, name='home'),

    path('foot_pound_calculator/', views.page_foot_pound_calc, name='foot_pound_calculator'),

    # page_loads_details
    path('loads/', views.page_loads, name='loads'),
    path('loads/<int:load_pk>', views.page_loads_details, name='loads'),
    path('loads/<str:load_type>', views.page_loads_by_type, name='loads'),

    path('estimated_dope/<int:load_pk>', views.page_estimated_dope, name='page_estimated_dope'),
    path('estimated_dope/', views.page_estimated_dope, name='page_estimated_dope'),

    path('firearm_detail/<int:firearm_pk>', views.page_firearm_detail, name='page_firearm_detail'),
    path('firearm_detail/', views.page_firearm_detail, name='page_firearm_detail'),

    path('caliber_detail/<int:caliber_pk>', views.page_caliber_detail, name='page_caliber_detail'),
    path('caliber_detail/', views.page_caliber_detail, name='page_caliber_detail'),

    path('toolbox/', views.home_create_view, name='create_home'),
    path('toolbox/create_caliber/', views.caliber_create_view, name='create_caliber'),
    path('toolbox/create_powder/', views.powder_create_view, name='create_powder'),
    path('toolbox/create_projectile/', views.projectile_create_view, name='create_projectile'),
    path('toolbox/create_firearm/', views.firearm_create_view, name='create_firearm'),

    path('docker/', views.docker_update_test, name='docker_update_test'),

]

