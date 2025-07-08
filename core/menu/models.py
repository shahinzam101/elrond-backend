# menu/models.py
from django.db import models
from django.core.validators import MinValueValidator
from restaurants.models import Restaurant


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="نام دسته‌بندی"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"
        ordering = ['name']

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    
    TYPE_CHOICES = [
        ('food', 'غذا'),
        ('drink', 'نوشیدنی'),
    ]
    
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="menu_items",
        verbose_name="رستوران"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="menu_items",
        verbose_name="دسته‌بندی"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="نام محصول"
    )
    item_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        verbose_name="نوع محصول"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="قیمت"
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name="موجود"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    class Meta:
        verbose_name = "آیتم منو"
        verbose_name_plural = "آیتم‌های منو"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"