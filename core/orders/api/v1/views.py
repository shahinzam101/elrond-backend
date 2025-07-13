from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from orders.models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from restaurants.models import Restaurant
from .permissions import IsRestaurantOwnerOrSuperuser
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import OrderFilter, OrderItemFilter



# ViewSet برای سفارش‌ها؛ اینجا می‌تونید سفارش‌ها رو مدیریت کنید و فیلترهای باحال بذارید :)
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsRestaurantOwnerOrSuperuser]  # فقط کاربرای لاگین‌شده و صاحب رستوران
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # فیلتر، جستجو و مرتب‌سازی
    filterset_class = OrderFilter  # فیلترهای پیشرفته از فایل filters.py
    search_fields = ['order_number', 'customer_name', 'customer_phone']  # جستجو بر اساس شماره سفارش، نام و تلفن مشتری
    ordering_fields = ['order_date', 'total', 'status']  # مرتب‌سازی بر اساس تاریخ، مبلغ کل یا وضعیت
    ordering = ['-order_date']  # پیش‌فرض مرتب‌سازی نزولی بر اساس تاریخ سفارش

    def get_queryset(self):
        # فقط سفارش‌های رستوران کاربر رو نشون می‌دیم، مگه اینکه سوپریوزر باشه
        user = self.request.user
        if user.is_superuser:
            return Order.objects.all()
        if hasattr(user, 'restaurant'):
            return Order.objects.filter(restaurant=user.restaurant)
        return Order.objects.none()  # اگه هیچی نبود، هیچی برنمی‌گردونیم!

# ViewSet برای آیتم‌های سفارش؛ اینجا آیتم‌ها رو مدیریت می‌کنید با کلی امکانات باحال!
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsRestaurantOwnerOrSuperuser]  # فقط کاربرای مجاز
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # فیلتر، جستجو و مرتب‌سازی فعاله
    filterset_class = OrderItemFilter  # فیلترهای پیشرفته برای آیتم‌ها
    search_fields = ['menu_item__name']  # جستجو بر اساس نام آیتم منو
    ordering_fields = ['quantity', 'total_price']  # مرتب‌سازی بر اساس تعداد یا قیمت کل
    ordering = ['id']  # پیش‌فرض مرتب‌سازی بر اساس آی‌دی

    def get_queryset(self):
        # فقط آیتم‌های مربوط به رستوران کاربر رو نشون می‌دیم، مگه اینکه سوپریوزر باشه
        user = self.request.user
        if user.is_superuser:
            return OrderItem.objects.all()
        if hasattr(user, 'restaurant'):
            return OrderItem.objects.filter(order__restaurant=user.restaurant)
        return OrderItem.objects.none()  # اگه دسترسی نداشت، هیچی نشون نمی‌دیم