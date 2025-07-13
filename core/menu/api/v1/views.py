from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from menu.models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer
from .filters import CategoryFilter, MenuItemFilter
from .permissions import IsRestaurantOwnerOrSuperuser

# ViewSet برای مدیریت دسته‌بندی‌ها؛ اینجا می‌تونید دسته‌بندی جدید بسازید یا لیست بگیرید :)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]  # فقط کاربران لاگین کرده دسترسی دارن
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # امکانات فیلتر، جستجو و مرتب‌سازی
    filterset_class = CategoryFilter
    search_fields = ['name']  # جستجو راحت بر اساس نام دسته‌بندی
    ordering_fields = ['name', 'is_active']  # مرتب‌سازی بر اساس نام یا فعال بودن
    ordering = ['name']  # پیش‌فرض مرتب‌سازی بر اساس نام

# ViewSet برای آیتم‌های منو؛ اینجا می‌تونید آیتم‌ها رو مدیریت کنید و کلی امکانات فیلتر دارید!
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated, IsRestaurantOwnerOrSuperuser]  # فقط کاربران احراز هویت شده می‌تونن اینجا باشن
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # فیلتر و جستجو و مرتب‌سازی فعال هست
    filterset_class = MenuItemFilter
    search_fields = ['name', 'restaurant__name']  # جستجو هم بر اساس نام آیتم و هم نام رستوران
    ordering_fields = ['name', 'price', 'created_at', 'is_available']  # مرتب‌سازی بر اساس این فیلدها
    ordering = ['name']  # پیش‌فرض مرتب‌سازی بر اساس نام آیتم

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return MenuItem.objects.all()

        if hasattr(user, 'restaurant'):
            return MenuItem.objects.filter(restaurant=user.restaurant)

        return MenuItem.objects.none()