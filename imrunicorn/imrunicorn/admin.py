from django.contrib import admin
from .models import PageCounter, PageHideList

# Register your models here.
admin.site.register(PageCounter)
admin.site.register(PageHideList)
