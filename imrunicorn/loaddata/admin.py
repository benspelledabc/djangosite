from django.contrib import admin
from .models import Powder, Projectile, HandLoad, EstimatedDope

# Register your models here.
admin.site.register(Powder)
admin.site.register(Projectile)
admin.site.register(HandLoad)
admin.site.register(EstimatedDope)

