from rest_framework import serializers
from .models import DockerHubWebhook


class DockerHubWebhookSerializer(serializers.ModelSerializer):
    class Meta:
        model = DockerHubWebhook
        fields = "__all__"

# class RandomInsultSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = RandomInsult
#         fields = "__all__"
