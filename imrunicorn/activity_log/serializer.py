from rest_framework import serializers
from .models import ActivityPhotoValidation, ActivityLog, Activity


# class ActivitySerializer(serializers.ModelSerializer):
class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        # fields = ('url', 'name', 'description', 'transaction_amount')


class ActivityPhotoValidationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivityPhotoValidation
        fields = '__all__'
        # fields = ('url', 'Blurb', 'Page_Link_From_Base')


class ActivityLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivityLog
        fields = '__all__'
        # fields = ('url', 'Blurb', 'Page_Link_From_Base')
