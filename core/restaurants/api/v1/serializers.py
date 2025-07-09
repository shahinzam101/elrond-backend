from rest_framework import serializers
from restaurants.models import Restaurant, RestaurantProfile


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name"]


class RestaurantProfileSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)
    manager_name = serializers.CharField(source='manager.full_name', read_only=True)
    


    class Meta:
        model = RestaurantProfile
        fields = [
            "id",
            "restaurant_name",  #  فقط نام رستوران نشون داده میشه
            "owner_name",
            "manager_name",
            "contact_email",
            "phone_number",
            "address",
            "logo",
        ]
