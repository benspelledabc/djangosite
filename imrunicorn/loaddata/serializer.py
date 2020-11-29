from rest_framework import serializers
from .models import Caliber, Firearm
from django.contrib.auth.models import User


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name')


class CaliberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Caliber
        fields = ('url', 'name', 'diameter', 'author_pk', 'is_approved')


# this doesn't like the OWNER object because it's not serialized yet
class FirearmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Firearm
        fields = ('url', 'manufacture', 'model', 'owner', 'barrel_length', 'caliber', 'inches_per_twist',
                  'clicks_from_bottom_to_zero_elevation', 'clicks_from_bottom_to_zero_windage', 'extra_info')
