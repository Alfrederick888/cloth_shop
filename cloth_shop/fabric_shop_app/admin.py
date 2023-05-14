from django.contrib import admin
from .models import *


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

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'status')




admin.site.register(Cloth, ClothAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Comment)
admin.site.register(Status)
