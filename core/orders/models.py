# orders/models.py
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from restaurants.models import Restaurant
from menu.models import MenuItem


class Order(models.Model):
    """مدل سفارش"""
    
    STATUS_CHOICES = [
        ('pending', 'در انتظار'),
        ('confirmed', 'تأیید شده'),
        ('completed', 'تکمیل شده'),
        ('cancelled', 'لغو شده'),
    ]
    
    ORDER_TYPE_CHOICES = [
        ('dine_in', 'تحویل حضوری'),
        ('delivery', 'تحویل غیر حضوری'),
    ]
    
    order_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="شماره سفارش"
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name="رستوران"
    )
    customer_name = models.CharField(
        max_length=100,
        verbose_name="نام مشتری"
    )
    customer_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="تلفن مشتری"
    )
    
    order_type = models.CharField(
        max_length=20,
        choices=ORDER_TYPE_CHOICES,
        default='dine_in',
        verbose_name="نوع سفارش"
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="وضعیت"
    )
    
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="جمع کل"
    )
    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="تخفیف"
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="مجموع نهایی"
    )
    
    customer_comment = models.TextField(
        blank=True,
        null=True,
        verbose_name="نظر مشتری"
    )
    
    order_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ سفارش"
    )
    completed_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="تاریخ تکمیل"
    )

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش‌ها"
        ordering = ['-order_date']

    def __str__(self):
        return f"سفارش {self.order_number} - {self.customer_name}"

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self.generate_order_number()
        
        self.total = self.subtotal - self.discount
        
        if self.status == 'completed' and not self.completed_at:
            self.completed_at = timezone.now()
            
        super().save(*args, **kwargs)

    def generate_order_number(self):
        """تولید شماره سفارش"""
        import random
        import string
        return ''.join(random.choices(string.digits, k=8))

    def calculate_subtotal(self):
        """محاسبه جمع کل از روی آیتم‌ها"""
        total = sum(item.total_price for item in self.items.all())
        self.subtotal = total
        return total


class OrderItem(models.Model):
    """آیتم‌های سفارش"""
    
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="سفارش"
    )
    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE,
        verbose_name="آیتم منو"
    )
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name="تعداد"
    )
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="قیمت واحد"
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="قیمت کل"
    )

    class Meta:
        verbose_name = "آیتم سفارش"
        verbose_name_plural = "آیتم‌های سفارش"

    def __str__(self):
        return f"{self.menu_item.name} x{self.quantity}"

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)