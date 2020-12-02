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
        fields = ('id', 'url', 'nickname', 'elevation', 'latitude', 'longitude')


class RemovalsByLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RemovalsByLocation
        fields = (
        'id', 'url', 'shooter', 'removal_date', 'removal_time', 'firearm', 'load', 'location', 'estimated_weight_lbs',
        'excessive_wound_cavity', 'shot_distance_yards', 'extra_info', 'kill_shot', 'kill_shot_two', 'sex')
