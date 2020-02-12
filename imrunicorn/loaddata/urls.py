from django.urls import path
from . import views

# router = routers.DefaultRouter()
# router.register('roll', views.RollView)
# router.register('student', views.StudentView)
# router.register('courses', views.CourseView)

app_name = 'load_data'
urlpatterns = [
    path('', views.page_loads, name='home'),
    path('loads/', views.page_loads, name='loads'),
    path('estimated_dope/<int:load_pk>', views.page_estimated_dope, name='page_estimated_dope'),
    # path('estimated_dope/<slug:load_pk>', views.page_estimated_dope, name='page_estimated_dope'),
    path('estimated_dope/', views.page_estimated_dope, name='page_estimated_dope'),
]

