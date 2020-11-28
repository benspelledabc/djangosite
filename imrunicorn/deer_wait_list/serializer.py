from rest_framework import serializers
from .models import Recipient, MeatCut, Flavor, RequestedOrder


class RecipientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipient
        fields = ('url', 'name', 'phone', 'email', 'perceived_thankfulness')


class MeatCutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MeatCut
        fields = ('url', 'name', 'level_of_effort')


class FlavorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flavor
        fields = ('url', 'name')


class RequestedOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequestedOrder
        fields = ('url', 'order_date', 'order_complete', 'recipient', 'notes', 'flavor', 'choice_cuts')
