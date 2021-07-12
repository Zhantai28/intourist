from django.contrib import admin
from django.db import models
from .models import Place, Feedback

# Register your models here.


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'created_at']
    readonly_fields = ['name', 'location', 'description']


admin.site.register(Place, PlaceAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['text', 'place', 'user', 'checked']
    list_display_links = ['place', 'text']
    list_editable = ['checked']
    list_filter = ['checked']
    search_fields = ['text', 'place__name',
                     'place__location', 'place__description']

    fields = ['user', 'place', 'text']
    readonly_fields = ['place', 'text']


admin.site.register(Feedback, FeedbackAdmin)
