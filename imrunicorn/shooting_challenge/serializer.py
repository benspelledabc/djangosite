from rest_framework import serializers
from .models import ChallengeEvent, ChallengePhoto


class ChallengePhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChallengePhoto
        fields = "__all__"


class ChallengeEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChallengeEvent
        fields = "__all__"

