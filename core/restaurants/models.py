from django.db import models



class Restaurant(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='اسم رستوران')

    def __str__(self):
        return self.name

class RestaurantProfile(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE, related_name="profile" , verbose_name= "رستوران" )
    owner_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="مالک")
    manager = models.OneToOneField(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name='restaurant_profile',
        verbose_name="مدیر",
        blank=True,
        null=True,
    )
    contact_email = models.EmailField(blank=True, null=True, verbose_name="ایمیل")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="تلفن")
    address = models.TextField(blank=True, null=True, verbose_name="آدرس")
    logo = models.ImageField(upload_to='restaurant_logos/', blank=True, null=True, verbose_name="لگو")

    class Meta:
        verbose_name = "رستوران"
        verbose_name_plural = "رستوران‌ها"
        ordering = ['restaurant']

    def __str__(self):
        return f"Profile of {self.restaurant.name}"
