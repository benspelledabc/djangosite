from django.urls import path
from . import views

# router = routers.DefaultRouter()
# router.register('roll', views.RollView)
# router.register('student', views.StudentView)
# router.register('courses', views.CourseView)

app_name = 'meme_leach'
urlpatterns = [
    path('', views.sample, name='home'),
]

