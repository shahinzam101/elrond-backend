from rest_framework import permissions
from menu.models import MenuItem

class IsRestaurantOwnerOrSuperuser(permissions.BasePermission):
    """
    فقط سوپریوزر یا صاحب رستوران آیتم منو اجازه دارد.
    """

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.is_superuser or hasattr(user, 'restaurant'))

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.is_superuser:
            return True

        if not hasattr(user, 'restaurant'):
            return False

        if isinstance(obj, MenuItem):
            return obj.restaurant == user.restaurant

        try:
            return obj.menuitem.restaurant == user.restaurant
        except AttributeError:
            return False
