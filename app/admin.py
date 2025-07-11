from django.contrib import admin
from django.utils.translation import gettext_lazy as _
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


class AboutAdmin(ImportExportModelAdmin, TranslatableAdmin):
    list_display = ('id', 'title')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image')
        }),
    )
    search_fields = ('translations__title', 'translations__description')
    ordering = ('id',)
    readonly_fields = ('id',)
    list_per_page = 10


admin.site.register(About, AboutAdmin)


class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    fieldsets = (
        (None, {
            'fields': ('name', 'image')
        }),
    )
    search_fields = ('name',)
    ordering = ('id',)
    readonly_fields = ('id',)
    list_per_page = 50


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(ImportExportModelAdmin, TranslatableAdmin):
    list_display = ('id', 'name', 'category')
    fieldsets = (
        (None, {
            'fields': (
                'name', 'description', 'features', 'category', 'image1', 'image2', 'image3', 'image4', 'subcategory')
        }),
    )
    search_fields = (
        'translations__name', 'translations__description', 'translations__features', 'category__translations__name')
    ordering = ('id',)
    readonly_fields = ('id',)
    list_per_page = 50


admin.site.register(Product, ProductAdmin)


class FaqAdmin(ImportExportModelAdmin, TranslatableAdmin):
    list_display = ('id', 'question')
    fieldsets = (
        (None, {
            'fields': ('question', 'answer')
        }),
    )
    search_fields = ('translations__question', 'translations__answer')
    ordering = ('id',)
    readonly_fields = ('id',)
    list_per_page = 10


admin.site.register(Faq, FaqAdmin)


class SubCategoryAdmin(TranslatableAdmin):
    list_display = ('get_name', 'parent')
    search_fields = ('translations__name',)

    fields = ('name', 'parent')

    def get_name(self, obj):
        return obj.safe_translation_getter('name', any_language=True)

    get_name.short_description = _('Name')


admin.site.register(SubCategory, SubCategoryAdmin)
