from django.contrib import admin
from .models import Harvests, HarvestPhoto, DeerManagementPermit

# Register your models here.
admin.site.register(Harvests)
admin.site.register(HarvestPhoto)
admin.site.register(DeerManagementPermit)
