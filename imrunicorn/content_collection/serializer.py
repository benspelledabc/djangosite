from rest_framework import serializers
from .models import RandomInsult, BuzzWordOrPhrase, SensorReadings


class RandomInsultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RandomInsult
        fields = "__all__"


class BuzzWordOrPhraseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuzzWordOrPhrase
        fields = "__all__"


class SensorReadingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorReadings
        # fields = "__all__"
        fields = ('read_datetime', 'sensor_location', 'sensor_model', 'celsius', 'fahrenheit', 'humidity')
