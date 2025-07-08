from django.contrib import admin
from .models import CustomUser
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'role', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('email', 'role')
    list_filter = ('is_active', 'is_staff', 'role')


admin.site.site_header = "💼 مدیریت کاربران"
admin.site.site_title = "💻 مدیریت کاربران"
admin.site.index_title = "🎯 داشبورد مدیریت"
