from rest_framework.response import Response
from datetime import datetime, date
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import redirect
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import permission_required
from rest_framework.permissions import IsAuthenticated

from announcements.models import WhatIsNew, MainPageBlurbs, PageBlurbOverrides, PageBlurbOverrides
from announcements.serializer import WhatIsNewSerializer, MainPageBlurbsSerializer, PageBlurbOverridesSerializer

# Create your views here.
# uses the standards from django for CRUD


class WhatIsNewView(viewsets.ModelViewSet):
    queryset = WhatIsNew.objects.all()
    serializer_class = WhatIsNewSerializer


class MainPageBlurbsView(viewsets.ModelViewSet):
    queryset = MainPageBlurbs.objects.all()
    serializer_class = MainPageBlurbsSerializer


class PageBlurbOverridesView(viewsets.ModelViewSet):
    queryset = PageBlurbOverrides.objects.all()
    serializer_class = PageBlurbOverridesSerializer
