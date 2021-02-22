from django.contrib import admin
from .models import Location, RemovalsByLocation, RemovalPhoto

# Register your models here.
admin.site.register(Location)
admin.site.register(RemovalsByLocation)
admin.site.register(RemovalPhoto)
