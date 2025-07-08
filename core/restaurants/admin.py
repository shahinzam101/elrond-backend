from django.contrib import admin
from .models import Restaurant, RestaurantProfile
# Register your models here.


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(RestaurantProfile)
class RestaurantProfileAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'owner_name', 'contact_email', 'phone_number')
    search_fields = ('restaurant__name', 'owner_name', 'contact_email')
