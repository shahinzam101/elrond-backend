from django.contrib import admin
from .models import Category, MenuItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'category', 'item_type', 'price', 'is_available')
    list_filter = ('item_type', 'is_available', 'restaurant', 'category')
    search_fields = ('name', 'restaurant__name', 'category__name')
    list_editable = ('is_available',)
    readonly_fields = ('created_at',)
    ordering = ('name',)
