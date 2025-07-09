from rest_framework import permissions

class IsOwnerOrSuperuser(permissions.BasePermission):
    """
    فقط سوپریوزر یا مالک رستوران پروفایل اجازه دسترسی دارد.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user and user.is_superuser:
            return True

        # فقط اجازه به پروفایل رستورانی که خود کاربر بهش متصل هست
        return obj.restaurant == user.restaurant
