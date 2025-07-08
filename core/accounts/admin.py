from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', "full_name",'role', 'restaurant', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'role')
    search_fields = ('email', 'role', 'restaurant__name')
    ordering = ('-date_joined',)

    readonly_fields = ('date_joined',)

    fieldsets = (
        ("اطلاعات ورود", {
            'fields': ('email', "full_name",'password')
        }),
        ("نقش و دسترسی", {
            'fields': ('role', 'restaurant', 'is_active', 'is_staff', 'is_superuser')
        }),
        ("اطلاعات دیگر", {
            'fields': ('date_joined',)
        }),
        ("مجوزها", {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions'),
        }),
    )

    def has_add_permission(self, request):
        """جلوگیری از ساخت کاربر جدید در ادمین (اختیاری)"""
        return True  # یا False اگه بخوای فقط از طریق ثبت‌نام ساخته بشن


# تنظیمات کلی پنل مدیریت
admin.site.site_header = "💼 مدیریت سامانه رستوران"
admin.site.site_title = "🍽️ پنل مدیریت"
admin.site.index_title = "🎯 داشبورد مدیریتی"
