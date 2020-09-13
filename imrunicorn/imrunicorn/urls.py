"""imrunicorn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('admin/', admin.site.urls),
    path('', views.page_home, name='home'),

    path('donate/cash_app/', views.page_cash_app, name='donate_cash_app'),
    path('donate/steel_targets/', views.page_donate_steel_targets, name='donate_steel_targets'),

    path('api/', include('api.urls')),

    # page_pi_endpoint
    path('pi_test/', views.page_pi_endpoint, name='pi_test'),

    path('days_since', views.page_days_since, name='days_since'),
    path('batf/', views.fetch_estimated_batf_days, name='fetch_estimated_batf_days'),

    path('blog/', views.page_blog_read, name='blog_read'),
    path('blog/add/', views.page_blog_add, name='blog_add'),

    path('load_data/', include('loaddata.urls')),
    path('farm_invite/', include('farminvite.urls')),
    path('news/', include('announcements.urls')),
    path('polls/', include('polls.urls')),
    path('shooting_logbook/', include('shooting_logbook.urls')),
    path('groundhog_logbook/', include('groundhog_logbook.urls')),

    path('deer_harvest_logbook/', include('deer_harvest_logbook.urls')),

    path('admin_toolbox/', include('admin_toolbox.urls')),

    path('status_watcher/', include('status_watcher.urls')),



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
handler500 = 'imrunicorn.views.handler500'
