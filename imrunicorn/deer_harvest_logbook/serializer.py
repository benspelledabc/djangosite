from rest_framework import serializers
from .models import Harvests, HarvestPhoto
from django.contrib.auth.models import User


class HarvestPhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HarvestPhoto
        fields = '__all__'
        # fields = ('url', 'photo_date')


class HarvestsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Harvests
        fields = '__all__'
        # fields = ('url', 'shooter', 'harvest_date', 'harvest_time', 'dnr_confirmation', 'harvest_score',
        #           'bonus_for_not_unpleasant', 'crop_damage_permit', 'firearm', 'load',
        #           'estimated_weight_lbs', 'shot_distance_yards', 'extra_info',
        #           'sex', 'kill_shot', 'kill_shot_two', 'removal_photos')
