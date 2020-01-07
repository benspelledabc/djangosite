from django.urls import path
from . import views

# router = routers.DefaultRouter()
# router.register('roll', views.RollView)
# router.register('student', views.StudentView)
# router.register('courses', views.CourseView)

urlpatterns = [
    path('', views.page_loads, name='home'),
    path('loads/', views.page_loads, name='loads'),
    path('estimated_dope/<int:load_pk>', views.page_estimated_dope, name='page_estimated_dope'),
    # path('estimated_dope/<slug:load_pk>', views.page_estimated_dope, name='page_estimated_dope'),
    path('estimated_dope/', views.page_estimated_dope, name='page_estimated_dope'),
    path('avgsdcalc/', views.page_avg_and_sd_calc, name='page_avg_and_sd_calc'),

    # page_estimated_dope
    # path('knownloads2/', views.page_broken, name='knownloads'),
]

