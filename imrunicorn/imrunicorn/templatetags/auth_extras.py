from django import template
from django.contrib.auth.models import Group
from django.template.defaultfilters import register
# from fontawesome.fields import IconField


@register.filter(name='has_group')
def has_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
    except Group.DoesNotExist:
        return False
    return group in user.groups.all()

