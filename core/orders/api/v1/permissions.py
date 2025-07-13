from rest_framework import permissions
from orders.models import Order, OrderItem

class IsRestaurantOwnerOrSuperuser(permissions.BasePermission):
    """
    فقط سوپریوزر یا صاحب رستوران مرتبط با سفارش اجازه دارد.
    """
    def has_object_permission(self, request, view, obj):
        user = request.user

        # سوپریوزرها دسترسی کامل دارند
        if user and user.is_superuser:
            return True

        # بررسی وجود رستوران برای کاربر
        if not hasattr(user, 'restaurant'):
            return False

        # اگر obj یک Order باشه
        if isinstance(obj, Order):
            return obj.restaurant == user.restaurant

        # اگر obj یک OrderItem باشه
        if isinstance(obj, OrderItem):
            return obj.order.restaurant == user.restaurant

        return False