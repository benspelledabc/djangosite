from rest_framework import serializers
from .models import RandomInsult, BuzzWordOrPhrase


class RandomInsultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RandomInsult
        fields = "__all__"


class BuzzWordOrPhraseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuzzWordOrPhrase
        fields = "__all__"
