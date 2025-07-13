from rest_framework import serializers
from orders.models import Order, OrderItem
from restaurants.models import Restaurant
from menu.models import MenuItem

class OrderItemSerializer(serializers.ModelSerializer):
    """سرایلایزر ساده برای آیتم‌های سفارش"""
    menu_item_name = serializers.CharField(source='menu_item.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'menu_item_name', 'quantity', 'unit_price', 'total_price']
        read_only_fields = ['unit_price', 'total_price']

class OrderSerializer(serializers.ModelSerializer):
    """سرایلایزر ساده برای سفارش"""
    items = OrderItemSerializer(many=True, read_only=True)
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'restaurant', 'restaurant_name', 'customer_name',
            'customer_phone', 'order_type', 'status', 'subtotal', 'discount',
            'total', 'customer_comment', 'order_date', 'completed_at', 'items'
        ]
        read_only_fields = ['order_number', 'subtotal', 'total', 'order_date', 'completed_at']