from rest_framework import permissions

class IsOwnerOrSuperuser(permissions.BasePermission):
    """
    فقط سوپریوزر یا مالک رستوران پروفایل اجازه دسترسی داره.
    """

    def has_object_permission(self, request, view, obj):
        # اگر سوپریوزره، دسترسی کامل داره
        if request.user and request.user.is_superuser:
            return True

        # اگر کاربر معمولیه، فقط اجازه داره پروفایل رستوران خودش رو ببینه
        return obj.restaurant.user == request.user
