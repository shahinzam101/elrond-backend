from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('total_price',)
    fields = ('menu_item', 'quantity', 'unit_price', 'total_price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'restaurant', 'customer_name', 'status', 'order_type', 'order_date', 'total')
    list_filter = ('status', 'order_type', 'restaurant')
    search_fields = ('order_number', 'customer_name', 'customer_phone')
    readonly_fields = ('order_number', 'order_date', 'completed_at', 'total')
    inlines = [OrderItemInline]

    fieldsets = (
        ('اطلاعات سفارش', {
            'fields': ('restaurant', 'order_number', 'status', 'order_type', 'order_date', 'completed_at')
        }),
        ('مشتری', {
            'fields': ('customer_name', 'customer_phone', 'customer_comment')
        }),
        ('پرداخت', {
            'fields': ('subtotal', 'discount', 'total')
        }),
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'menu_item', 'quantity', 'unit_price', 'total_price')
    list_filter = ('menu_item',)
    search_fields = ('order__order_number', 'menu_item__name')
