from rest_framework import serializers
from .models import RandomInsult


class RandomInsultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RandomInsult
        fields = "__all__"
