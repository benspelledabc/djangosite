from django.contrib import admin
from .models import ShotCollection, ShotEntry, Location

# Register your models here.
admin.site.register(ShotCollection)
admin.site.register(ShotEntry)
admin.site.register(Location)
