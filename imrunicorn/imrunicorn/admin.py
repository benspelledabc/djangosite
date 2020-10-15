from django.contrib import admin
from .models import PageCounter, PageHideList, UserProfile

# Register your models here.
admin.site.register(PageCounter)
admin.site.register(PageHideList)
admin.site.register(UserProfile)
