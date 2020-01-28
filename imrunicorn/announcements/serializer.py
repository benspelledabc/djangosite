from rest_framework import serializers
from .models import WhatIsNew


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WhatIsNew
        fields = ('url', 'Date', 'Blurb', 'Body', 'Published')
