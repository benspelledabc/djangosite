from django.contrib import admin
from .models import Powder, Projectile, HandLoad, EstimatedDope, Firearm, Caliber

# Register your models here.
admin.site.register(Powder)
admin.site.register(Projectile)
admin.site.register(HandLoad)
admin.site.register(EstimatedDope)
admin.site.register(Firearm)
admin.site.register(Caliber)

