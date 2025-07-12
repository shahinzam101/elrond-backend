from django_filters import rest_framework as filters
from menu.models import Category, MenuItem

class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')  # فیلتر نام با جستجوی غیرحساس به حروف
    is_active = filters.BooleanFilter()  # فیلتر برای وضعیت فعال بودن

    class Meta:
        model = Category
        fields = ['name', 'is_active']

class MenuItemFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')  # فیلتر نام با جستجوی غیرحساس به حروف
    item_type = filters.ChoiceFilter(choices=MenuItem.TYPE_CHOICES)  # فیلتر بر اساس نوع آیتم
    price_min = filters.NumberFilter(field_name='price', lookup_expr='gte')  # حداقل قیمت
    price_max = filters.NumberFilter(field_name='price', lookup_expr='lte')  # حداکثر قیمت
    is_available = filters.BooleanFilter()  # فیلتر برای وضعیت موجود بودن
    restaurant = filters.NumberFilter(field_name='restaurant__id')  # فیلتر بر اساس ID رستوران
    category = filters.NumberFilter(field_name='category__id')  # فیلتر بر اساس ID دسته‌بندی

    class Meta:
        model = MenuItem
        fields = ['name', 'item_type', 'price_min', 'price_max', 'is_available', 'restaurant', 'category']