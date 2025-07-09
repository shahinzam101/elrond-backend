from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from restaurants.models import Restaurant, RestaurantProfile


@receiver(post_save, sender=CustomUser)
def create_restaurant_and_profile(sender, instance, created, **kwargs):
    """
    وقتی یک کاربر جدید ساخته می‌شود و نقش او 'manager' است:
    - یک رستوران (با نام دلخواه کاربر) ساخته می‌شود
    - رستوران به کاربر متصل می‌شود
    - یک پروفایل رستوران نیز ایجاد می‌شود
    """
    if created and instance.role == 'manager':
        # نام رستوران از متغیر موقتی گرفته می‌شود (در serializer تنظیم شده)
        restaurant_name = getattr(instance, '_restaurant_name', f"رستوران {instance.full_name}")

        # جلوگیری از تکرار رستوران
        restaurant, _ = Restaurant.objects.get_or_create(name=restaurant_name)

        # اتصال رستوران به کاربر
        instance.restaurant = restaurant
        instance.save()

        # ساخت پروفایل رستوران فقط اگر قبلاً ساخته نشده
        if not hasattr(restaurant, 'profile'):
            RestaurantProfile.objects.create(restaurant=restaurant, owner_name=instance.full_name)