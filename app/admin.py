from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from parler.admin import TranslatableAdmin
from app.models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'country')
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'country', 'message')
        }),
    )
    search_fields = ('name', 'email', 'country')
    ordering = ('id',)
    readonly_fields = ('id',)
    list_per_page = 10

admin.site.register(Contact, ContactAdmin)

class CategoryAdmin(ImportExportModelAdmin, TranslatableAdmin):
    list_display = ('id', 'name')
    fieldsets = (
        (None, {
            'fields': ('name', 'image')
        }),
    )
    search_fields = ('translations__name',)
    ordering = ('id',)
    readonly_fields = ('id',)
    list_per_page = 10

admin.site.register(Category, CategoryAdmin)