from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.


class CustomUserManger(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", "admin")
        return self.create_user(email, password, **extra_fields)
    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('manager', 'مدیر'),
        ('viewer', 'بیننده'),
    )

    email = models.EmailField(unique=True, verbose_name="ایمیل")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='viewer', verbose_name="نقش")
    # restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)

    is_active = models.BooleanField(default=True, verbose_name="فعال")
    is_staff = models.BooleanField(default=False, verbose_name="کارمند")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت نام")


    objects = CustomUserManger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 
    def __str__(self):
        return f"{self.email}"
    

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

