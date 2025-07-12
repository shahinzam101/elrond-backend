from rest_framework import serializers
from menu.models import Category, MenuItem
from restaurants.models import Restaurant

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'is_active']
        read_only_fields = ['id']

class MenuItemSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = MenuItem
        fields = [
            'id',
            'restaurant',
            'restaurant_name',
            'category',
            'category_name',
            'name',
            'item_type',
            'price',
            'is_available',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']