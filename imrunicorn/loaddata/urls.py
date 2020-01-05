from django.urls import path
from . import views

# router = routers.DefaultRouter()
# router.register('roll', views.RollView)
# router.register('student', views.StudentView)
# router.register('courses', views.CourseView)

urlpatterns = [
    path('', views.page_loads, name='home'),
    path('loads/', views.page_loads, name='loads'),
    path('avgsdcalc/', views.page_avg_and_sd_calc, name='page_avg_and_sd_calc'),

    # path('knownloads2/', views.page_broken, name='knownloads'),
]
