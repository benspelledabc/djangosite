from django.contrib import admin
from .models import WhatIsNew, MainPageBlurbs, PageBlurbOverrides

# Register your models here.
admin.site.register(WhatIsNew)
# admin.site.register(MainPageBlurbs)
admin.site.register(PageBlurbOverrides)
