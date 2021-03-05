from abc import ABC

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from imrunicorn.models import UserProfile
from django.contrib.auth.models import User, Group


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        read_only_fields = ('preferred_display_name',)
        fields = "__all__"
        # exclude = ('',)    # user  ?
        # fields = ('preferred_display_name',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name',)


# default password for resets? "pbkdf2_sha256$180000$zj8vzjUxyqWJ$+KjTF7Xf9HSFK0HQ5pmwQb0Hf1D/n4/i96U7p3JzLkc="
# old wow password for Dark Ascension coms
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # groups = GroupSerializer(many=True)
    # profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('url',
                  'last_login',
                  'is_superuser',
                  'is_staff',
                  'is_active',
                  'username',
                  'password',
                  # 'profile',
                  # 'user_profile',
                  'first_name',
                  'last_name',
                  'email',
                  'date_joined',
                  # 'groups',
                  # 'user_permissions'
                  )
        # fields = "__all__"

