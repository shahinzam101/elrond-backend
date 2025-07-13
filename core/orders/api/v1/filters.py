from django_filters import rest_framework as filters
from orders.models import Order, OrderItem

# فیلتر برای سفارش‌ها؛ راحت می‌تونید با اینا فیلتر کنید :)
class OrderFilter(filters.FilterSet):
    class Meta:
        model = Order
        fields = {
            'status': ['exact'],  # فیلتر دقیق برای وضعیت
            'order_type': ['exact'],  # فیلتر دقیق برای نوع سفارش
            'restaurant': ['exact'],  # فیلتر بر اساس رستوران
            'order_date': ['gte', 'lte'],  # فیلتر برای بازه تاریخ سفارش
        }

# فیلتر برای آیتم‌های سفارش؛ ساده و کاربردی!
class OrderItemFilter(filters.FilterSet):
    class Meta:
        model = OrderItem
        fields = {
            'order': ['exact'],  # فیلتر بر اساس سفارش
            'menu_item': ['exact'],  # فیلتر بر اساس آیتم منو
        }