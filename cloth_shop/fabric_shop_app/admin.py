from django.contrib import admin
from .models import Cloth, Category, Status, Order, Comment


@admin.register(Cloth)
class ClothAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description',
        'cat', 'color',
        'quantity', 'is_published',
        'picture')
    list_display_links = ('name',)
    search_fields = ('name', 'color')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone',
                    'status', 'comment_text')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_binding', 'comment_text')
    list_display_links = ('comment_binding',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('Status_name',)
