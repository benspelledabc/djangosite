from rest_framework import serializers
from .models import RemovalsByLocation, Location
from django.contrib.auth.models import User


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('url', 'nickname', 'elevation', 'latitude', 'longitude')


class RemovalsByLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RemovalsByLocation
        fields = "__all__"
        # fields = (
        #     'url', 'shooter', 'removal_date', 'removal_time', 'firearm', 'load', 'location',
        #     'estimated_weight_lbs',
        #     'excessive_wound_cavity', 'shot_distance_yards', 'yards_ran', 'extra_info', 'kill_shot',
        #     'kill_shot_two', 'sex')
