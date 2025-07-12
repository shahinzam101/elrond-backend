from restaurants.models import Restaurant, RestaurantProfile
from rest_framework import permissions

class IsOwnerOrSuperuser(permissions.BasePermission):
    """
    فقط سوپریوزر یا صاحب رستوران اجازه دارد.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user and user.is_superuser:
            return True

        if not hasattr(user, 'restaurant'):
            return False

        # اگر obj یک Restaurant باشه
        if isinstance(obj, Restaurant):
            return obj == user.restaurant

        # اگر obj یک RestaurantProfile باشه
        if isinstance(obj, RestaurantProfile):
            return obj.restaurant == user.restaurant

        return False
