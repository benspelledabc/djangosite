from django.contrib import admin
from .models import Activity, ActivityLog, ActivityPhotoValidation

# Register your models here.
admin.site.register(Activity)
admin.site.register(ActivityLog)
admin.site.register(ActivityPhotoValidation)
