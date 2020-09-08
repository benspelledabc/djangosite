from django.contrib import admin
from .models import Recipient, MeatCut, RequestedOrder, Flavor

admin.site.register(Recipient)
admin.site.register(MeatCut)
admin.site.register(RequestedOrder)
admin.site.register(Flavor)
