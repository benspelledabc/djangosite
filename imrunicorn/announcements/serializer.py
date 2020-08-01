from rest_framework import serializers
from .models import WhatIsNew, MainPageBlurbs, PageBlurbOverrides


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WhatIsNew
        fields = ('url', 'Date', 'Blurb', 'Body', 'Image_One', 'Published', 'Is_Sticky')


class WhatIsNewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WhatIsNew
        fields = ('url', 'Date', 'Blurb', 'Body', 'Image_One', 'Published', 'Is_Sticky')


class MainPageBlurbsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MainPageBlurbs
        fields = ('Blurb', 'Is_Active')


class PageBlurbOverridesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PageBlurbOverrides
        fields = ('Blurb', 'Page_Link_From_Base')


