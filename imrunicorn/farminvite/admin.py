from django.contrib import admin
from .models import InviteListing, PackingListItem, PackingList

# Register your models here.
admin.site.register(InviteListing)
admin.site.register(PackingListItem)
admin.site.register(PackingList)
