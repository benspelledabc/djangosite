from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions, \
    DjangoObjectPermissions, DjangoModelPermissionsOrAnonReadOnly, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.response import Response
from datetime import datetime, date
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.decorators import action
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

from groundhog_logbook.models import Location, RemovalsByLocation
from groundhog_logbook.serializer import LocationSerializer, RemovalsByLocationSerializer

from activity_log.models import ActivityPhotoValidation, ActivityLog, Activity
from activity_log.serializer import ActivitySerializer, ActivityLogSerializer, ActivityPhotoValidationSerializer

from imrunicorn.functions import step_hit_count_by_page, get_weather

from groundhog_logbook.functions import all_groundhog_removals, all_groundhog_removals_by_shooter, \
    all_groundhog_hole_locations, groundhog_removal_scoreboard, \
    groundhogs_by_hour_of_day, groundhogs_by_hour_of_day_by_sex, groundhogs_by_sex, groundhogs_count_by_sex, \
    groundhog_removal_scoreboard_annual


class Owner(viewsets.ModelViewSet):
    # require user to be logged on.
    permission_classes = (IsAuthenticated,)
    # fetch data
    queryset = User.objects.all()
    serializer_class = OwnerSerializer


# ############### activity_log ###############
class ActivityPhotoValidationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = ActivityPhotoValidation.objects.all()
    serializer_class = ActivityPhotoValidationSerializer


class ActivityLogViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer

    @action(detail=False)
    def approval_pending(self, request):
        queryset = ActivityLog.objects.filter(
            Q(approved=False))
        result = self.paginate_queryset(queryset)
        if result is not None:
            serializer = self.get_serializer(result, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def approval_complete(self, request):
        queryset = ActivityLog.objects.filter(
            Q(approved=True))
        result = self.paginate_queryset(queryset)
        if result is not None:
            serializer = self.get_serializer(result, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ActivityViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    @action(detail=False)
    def sfw_all(self, request):
        queryset = Activity.objects.filter(
            Q(sfw=True))
        result = self.paginate_queryset(queryset)
        if result is not None:
            serializer = self.get_serializer(result, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def tasks_all(self, request):
        queryset = Activity.objects.filter(
            Q(transaction_amount__gt=0))
        result = self.paginate_queryset(queryset)
        if result is not None:
            serializer = self.get_serializer(result, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def rewards_all(self, request):
        queryset = Activity.objects.filter(
            Q(transaction_amount__lte=0))
        result = self.paginate_queryset(queryset)
        if result is not None:
            serializer = self.get_serializer(result, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def random_task_all(self, request):
        queryset = Activity.objects.filter(
            Q(transaction_amount__gt=0)).order_by('?')[:1]
        result = self.paginate_queryset(queryset)
        if result is not None:
            serializer = self.get_serializer(result, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def random_task_sfw(self, request):
        queryset = Activity.objects.filter(
            Q(transaction_amount__gt=0, sfw=True)).order_by('?')[:1]
        result = self.paginate_queryset(queryset)
        if result is not None:
            serializer = self.get_serializer(result, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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
    queryset = HandLoad.objects.all().order_by('-id')
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
    # permission_classes = (IsAdminUser,)
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    permission_classes = (DjangoObjectPermissions,)

    queryset = WhatIsNew.objects.all()
    serializer_class = WhatIsNewSerializer

    @action(detail=False)
    def random_one(self, request):
        queryset = WhatIsNew.objects.order_by('?')[:1]
        result = self.paginate_queryset(queryset)
        if result is not None:
            serializer = self.get_serializer(result, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def sticky(self, request):
        queryset = WhatIsNew.objects.filter(
            Q(Is_Sticky=True))
        result = self.paginate_queryset(queryset)
        if result is not None:
            serializer = self.get_serializer(result, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def published(self, request):
        queryset = WhatIsNew.objects.filter(
            Q(Published=True))
        result = self.paginate_queryset(queryset)
        if result is not None:
            serializer = self.get_serializer(result, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def not_published(self, request):
        queryset = WhatIsNew.objects.filter(
            Q(Published=False))
        result = self.paginate_queryset(queryset)
        if result is not None:
            serializer = self.get_serializer(result, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class MainPageBlurbsView(viewsets.ModelViewSet):
    queryset = MainPageBlurbs.objects.all()
    serializer_class = MainPageBlurbsSerializer


class PageBlurbOverridesView(viewsets.ModelViewSet):
    queryset = PageBlurbOverrides.objects.all()
    serializer_class = PageBlurbOverridesSerializer


# ############### groundhog_logbook ###############
class LocationView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class RemovalsByLocationView(viewsets.ModelViewSet):
    queryset = RemovalsByLocation.objects.all()
    serializer_class = RemovalsByLocationSerializer
