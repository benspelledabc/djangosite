from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

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
# from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from announcements.models import WhatIsNew, MainPageBlurbs, PageBlurbOverrides
from announcements.serializer import WhatIsNewSerializer, MainPageBlurbsSerializer, PageBlurbOverridesSerializer

from deer_wait_list.models import Recipient, MeatCut, Flavor, RequestedOrder
from deer_wait_list.serializer import RecipientSerializer, MeatCutSerializer, FlavorSerializer, RequestedOrderSerializer

from loaddata.models import Caliber, Firearm, Powder, Projectile, Brass, Primer, HandLoad, EstimatedDope
from loaddata.serializer import CaliberSerializer, FirearmSerializer, OwnerSerializer, PowderSerializer, \
    ProjectileSerializer, BrassSerializer, PrimerSerializer, HandLoadSerializer, EstimatedDopeSerializer


class Owner(viewsets.ModelViewSet):
    # require user to be logged on.
    permission_classes = (IsAuthenticated,)
    # fetch data
    queryset = User.objects.all()
    serializer_class = OwnerSerializer


# ############### loaddata ###############
class LoadDataCaliber(viewsets.ModelViewSet):
    # require user to be logged on.
    # permission_classes = (IsAuthenticated,)
    # fetch data
    queryset = Caliber.objects.all()
    serializer_class = CaliberSerializer


class LoadDataFirearm(viewsets.ModelViewSet):
    # require user to be logged on.
    # permission_classes = (IsAuthenticated,)
    # fetch data
    queryset = Firearm.objects.all()
    serializer_class = FirearmSerializer


class LoadDataPowder(viewsets.ModelViewSet):
    # require user to be logged on.
    # permission_classes = (IsAuthenticated,)
    # fetch data
    queryset = Powder.objects.all()
    serializer_class = PowderSerializer


class LoadDataProjectile(viewsets.ModelViewSet):
    # require user to be logged on.
    # permission_classes = (IsAuthenticated,)
    # fetch data
    queryset = Projectile.objects.all()
    serializer_class = ProjectileSerializer


class LoadDataBrass(viewsets.ModelViewSet):
    # require user to be logged on.
    # permission_classes = (IsAuthenticated,)
    # fetch data
    queryset = Brass.objects.all()
    serializer_class = BrassSerializer


class LoadDataPrimer(viewsets.ModelViewSet):
    # require user to be logged on.
    # permission_classes = (IsAuthenticated,)
    # fetch data
    queryset = Primer.objects.all()
    serializer_class = PrimerSerializer


class LoadDataHandLoad(viewsets.ModelViewSet):
    # require user to be logged on.
    permission_classes = (IsAuthenticated,)
    # fetch data
    queryset = HandLoad.objects.all()
    serializer_class = HandLoadSerializer


class LoadDataEstimatedDope(viewsets.ModelViewSet):
    # require user to be logged on.
    # permission_classes = (IsAuthenticated,)
    # fetch data
    queryset = EstimatedDope.objects.all()
    serializer_class = EstimatedDopeSerializer


# ############### Deer Wait List ###############
class DeerWaitListRecipient(viewsets.ModelViewSet):
    # require user to be logged on.
    permission_classes = (IsAuthenticated,)
    # fetch data
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


class DeerWaitListMeatCut(viewsets.ModelViewSet):
    # require user to be logged on.
    # permission_classes = (IsAuthenticated,)
    # fetch data
    queryset = MeatCut.objects.all()
    serializer_class = MeatCutSerializer


class DeerWaitListFlavor(viewsets.ModelViewSet):
    # require user to be logged on.
    # permission_classes = (IsAuthenticated,)
    # fetch data
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer


class DeerWaitListRequestedOrder(viewsets.ModelViewSet):
    # require user to be logged on.
    # permission_classes = (IsAuthenticated,)
    # fetch data
    queryset = RequestedOrder.objects.all()
    # serializer_class = FlavorSerializer
    serializer_class = RequestedOrderSerializer


# ############### announcements ###############
class WhatIsNewView(viewsets.ModelViewSet):
    queryset = WhatIsNew.objects.all()
    serializer_class = WhatIsNewSerializer


class MainPageBlurbsView(viewsets.ModelViewSet):
    queryset = MainPageBlurbs.objects.all()
    serializer_class = MainPageBlurbsSerializer


class PageBlurbOverridesView(viewsets.ModelViewSet):
    queryset = PageBlurbOverrides.objects.all()
    serializer_class = PageBlurbOverridesSerializer
