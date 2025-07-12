from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from menu.models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer
from .filters import CategoryFilter, MenuItemFilter

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CategoryFilter
    search_fields = ['name']  # جستجو بر اساس نام دسته‌بندی
    ordering_fields = ['name', 'is_active']  # مرتب‌سازی بر اساس نام و وضعیت فعال بودن
    ordering = ['name']  # مرتب‌سازی پیش‌فرض

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MenuItemFilter
    search_fields = ['name', 'restaurant__name']  # جستجو بر اساس نام آیتم و نام رستوران
    ordering_fields = ['name', 'price', 'created_at', 'is_available']  # مرتب‌سازی بر اساس این فیلدها
    ordering = ['name']  # مرتب‌سازی پیش‌فرض

    def get_queryset(self):
        # فیلتر اختیاری بر اساس query params برای restaurant_id و category_id
        queryset = super().get_queryset()
        restaurant_id = self.request.query_params.get('restaurant_id')
        category_id = self.request.query_params.get('category_id')
        
        if restaurant_id:
            queryset = queryset.filter(restaurant_id=restaurant_id)
        if category_id:
            queryset = queryset.filter(category_id=category_id)
            
        return queryset