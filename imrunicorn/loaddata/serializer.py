from rest_framework import serializers
from .models import Caliber, Firearm, Powder, Projectile, Brass, Primer, HandLoad, EstimatedDope
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


class PowderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Powder
        fields = ('url', 'name', 'is_smokeless', 'buy_link', 'lbs_on_hand', 'author_pk', 'is_approved')


class ProjectileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projectile
        fields = ('url', 'Manufacture', 'Name', 'WeightGR', 'Diameter', 'Ballistic_Coefficient', 'projectiles_on_hand',
                  'buy_link', 'author_pk', 'is_approved')


class BrassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brass
        fields = ('url', 'caliber', 'manufacture', 'brass_on_hand', 'buy_link', 'author_pk', 'is_approved',)


class PrimerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Primer
        fields = ('url', 'manufacture', 'description', 'units_on_hand', 'buy_link', 'author_pk', 'is_approved',)


class HandLoadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HandLoad
        fields = (
            'url', 'powder', 'Powder_Charge', 'firearm', 'projectile', 'brass', 'primer', 'Velocity', 'Is_Estimated',
            'Standard_Deviation', 'Extreme_Spread', 'Is_Sheriff_Load', 'Confirmed_Splat_Factor', 'Group_Size',
            'Group_Picture', 'Notes')


class EstimatedDopeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EstimatedDope
        fields = (
            'url', )
