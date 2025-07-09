from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    restaurant_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'full_name', 'password', 'restaurant_name']

    def create(self, validated_data):
        restaurant_name = validated_data.pop('restaurant_name')
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            full_name=validated_data.get('full_name', ''),
            role='manager',  # نقش ثابت به 'مدیر'
        )
        # اتصال نام رستوران به کاربر برای استفاده در سیگنال
        user._restaurant_name = restaurant_name
        return user
