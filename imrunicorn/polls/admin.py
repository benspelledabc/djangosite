# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Choice, Poll


class ChoiceInline(admin.TabularInline):
    model = Choice
    readonly_fields = ('votes',)
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['question', 'start_date', 'end_date'],
        }),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'start_date', 'end_date',)
    search_fields = ['question']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
