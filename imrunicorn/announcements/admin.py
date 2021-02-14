from django.contrib import admin
from .models import WhatIsNew, MainPageBlurbs, PageBlurbOverrides, PageSecret

# Register your models here.
admin.site.register(WhatIsNew)
admin.site.register(MainPageBlurbs)
admin.site.register(PageBlurbOverrides)
admin.site.register(PageSecret)
