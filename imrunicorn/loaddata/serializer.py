from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import Caliber, Firearm, Powder, Projectile, Brass, Primer, HandLoad, EstimatedDope
from imrunicorn.models import UserProfile

from django.contrib.auth.models import User, Group

# xxx_changed_from_HyperlinkedModelSerializer_to_ModelSerializer


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('preferred_display_name',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name',)


class OwnerSerializer(serializers.ModelSerializer):
    # owner_display_name = UserProfileSerializer()
    # user_profile = UserProfileSerializer(many=False)
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id',
                  'last_login',
                  'is_superuser',
                  'username',
                  # 'user_profile',
                  'first_name',
                  'last_name',
                  'email',
                  'is_staff',
                  'is_active',
                  'date_joined',
                  'groups',
                  'user_permissions'
                  )
        # fields = "__all__"


class CaliberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caliber
        fields = "__all__"
        # fields = ('url', 'name', 'diameter', 'author_pk', 'is_approved')


class FirearmSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
    caliber = CaliberSerializer()

    class Meta:
        model = Firearm
        fields = "__all__"
        # fields = ('url', 'manufacture', 'model', 'owner', 'barrel_length', 'caliber', 'inches_per_twist',
        #           'clicks_from_bottom_to_zero_elevation', 'clicks_from_bottom_to_zero_windage', 'extra_info')


class PowderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Powder
        fields = "__all__"
        # fields = ('url', 'name', 'is_smokeless', 'buy_link', 'lbs_on_hand', 'author_pk', 'is_approved')


class ProjectileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projectile
        fields = "__all__"
        # fields = ('url', 'Manufacture', 'Name', 'WeightGR', 'Diameter', 'Ballistic_Coefficient',
        #     'projectiles_on_hand', 'buy_link', 'author_pk', 'is_approved')


class BrassSerializer(serializers.ModelSerializer):
    caliber = CaliberSerializer()

    class Meta:
        model = Brass
        fields = "__all__"
        # fields = ('url', 'caliber', 'manufacture', 'brass_on_hand', 'buy_link', 'author_pk', 'is_approved',)


class PrimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Primer
        fields = "__all__"
        # fields = ('url', 'manufacture', 'description', 'units_on_hand', 'buy_link', 'author_pk', 'is_approved',)


# class HandLoadSerializer(serializers.ModelSerializer):
class HandLoadSerializer(serializers.ModelSerializer):
    powder = PowderSerializer()
    firearm = FirearmSerializer()
    projectile = ProjectileSerializer()
    brass = BrassSerializer()
    primer = PrimerSerializer()

    class Meta:
        model = HandLoad
        # fields = (
        #     'id', 'url', 'powder', 'Powder_Charge', 'firearm', 'projectile', 'brass', 'primer', 'Velocity',
        #     'Is_Estimated', 'Standard_Deviation', 'Extreme_Spread', 'Is_Sheriff_Load', 'Confirmed_Splat_Factor',
        #     'Group_Size', 'Group_Picture', 'Notes')
        fields = "__all__"


class EstimatedDopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstimatedDope
        fields = "__all__"
        # fields = (
        #     'url', 'hand_load',
        #     'moa_100', 'moa_125', 'moa_150', 'moa_175',
        #     'moa_200', 'moa_225', 'moa_250', 'moa_275',
        #     'moa_300', 'moa_325', 'moa_350', 'moa_375',
        #     'moa_400', 'moa_425', 'moa_450', 'moa_475',
        #     'moa_500', 'moa_525', 'moa_550', 'moa_575',
        #     'moa_600', 'moa_625', 'moa_650', 'moa_675',
        #     'moa_700', 'moa_725', 'moa_750', 'moa_775',
        #     'moa_800', 'moa_825', 'moa_850', 'moa_875',
        #     'moa_900', 'moa_925', 'moa_950', 'moa_975',
        #     'moa_1000', 'moa_1025', 'moa_1050', 'moa_1075',
        # )
