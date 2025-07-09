from django.contrib import admin
from .models import Restaurant, RestaurantProfile

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(RestaurantProfile)
class RestaurantProfileAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'owner_name', 'contact_email', 'phone_number')
    search_fields = ('restaurant__name', 'owner_name', 'phone_number')
    list_filter = ('restaurant__name',)
    readonly_fields = ('logo_preview',)

    fieldsets = (
        (None, {
            'fields': ('restaurant', 'owner_name', 'contact_email', 'phone_number', 'address')
        }),
        ("لوگو", {
            'fields': ('logo', 'logo_preview'),
        }),
    )

    def logo_preview(self, obj):
        if obj.logo:
            return f'<img src="{obj.logo.url}" width="100" style="border-radius:8px" />'
        return "بدون لوگو"
    logo_preview.allow_tags = True
    logo_preview.short_description = "پیش‌نمایش لوگو"
