from rest_framework import serializers
from .models import LeachedMeme, LeachedMemePreview


class LeachedMemePreviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LeachedMemePreview
        fields = "__all__"


class LeachedMemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LeachedMeme
        fields = "__all__"
