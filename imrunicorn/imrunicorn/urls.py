from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime
from django.conf import settings
# from . import forms, views
from announcements.get_news import get_news, get_version_json
from django.conf import settings
from django.conf.urls.static import static
from . import forms, views


# app_name = 'base_skipped_for_now'
urlpatterns = [

    path('test/', views.page_test_layout, name='test_layout'),

    path('api-auth/', include('rest_framework.urls')),
    path('api/weather/', views.page_api_weather, name='page_api_weather'),
    path('qr/about/', views.page_qr_about, name='qr_about'),
    path('admin/', admin.site.urls),
    path('', views.page_home, name='home'),

    path('access_denied_groups', views.page_access_denied_groups, name='access_denied_groups'),

    path('page_hits/', views.page_page_hits, name='page_hits'),

    path('activity_log/', include('activity_log.urls')),
    path('announcements/', include('announcements.urls')),
    path('api/', include('api.urls')),
    path('load_data/', include('loaddata.urls')),
    path('farm_invite/', include('farminvite.urls')),
    path('polls/', include('polls.urls')),
    path('shooting_logbook/', include('shooting_logbook.urls')),
    path('groundhog_logbook/', include('groundhog_logbook.urls')),
    path('deer_harvest_logbook/', include('deer_harvest_logbook.urls')),
    path('deer_wait_list/', include('deer_wait_list.urls')),
    path('admin_toolbox/', include('admin_toolbox.urls')),
    path('status_watcher/', include('status_watcher.urls')),
    path('content_collection/', include('content_collection.urls')),
    path('call_of_the_wild/', include('call_of_the_wild.urls')),
    path('shooting_challenge/', include('shooting_challenge.urls')),
    path('dcsa_info/', include('dcsa_info.urls')),


    # path('contact/', views.contact, name='contact'),
    # path('about/', views.about, name='about'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('login/',
         LoginView.as_view
             (
             template_name='imrunicorn/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log In',
                 'copy_year': datetime.now().year,
                 'release': get_version_json(),
                 'blurb': 'I am not allowing new accounts at this time.',
                 'no_accounts_blurb': 'If you have an account and need a reset, you know how to reach me..',
             }
         ),
         name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # https://docs.djangoproject.com/en/2.0/topics/http/views/#customizing-error-views
# handler404 = 'YOUR_APP_NAME.views.handler404'

handler404 = 'imrunicorn.views.handler404'
handler403 = 'imrunicorn.views.handler403'
handler500 = 'imrunicorn.views.handler500'
