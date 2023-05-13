from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Cloth, Category


class ClothAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'cat', 'color', 'quantity', 'is_published', 'picture')
    list_display_links = ('name',)
    search_fields = ('name', 'color')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Cloth, ClothAdmin)
admin.site.register(Category, CategoryAdmin)
