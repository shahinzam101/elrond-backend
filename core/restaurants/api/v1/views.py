from rest_framework import viewsets, filters, serializers
from restaurants.models import Restaurant, RestaurantProfile
from .serializers import RestaurantProfileSerializer, RestaurantSerializer
from .permissions import IsOwnerOrSuperuser
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from restaurants.models import Restaurant
from .serializers import RestaurantSerializer
from .permissions import IsOwnerOrSuperuser

class RestaurantsViewSet(viewsets.ModelViewSet):
    """
    فقط سوپریوزر می‌تواند همه رستوران‌ها را ببیند.
    کاربران عادی فقط رستوران خودشان را می‌بینند.
    """
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrSuperuser]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]

    def get_queryset(self):
        user = self.request.user

        # سوپریوزر می‌تونه همه رستوران‌ها رو ببینه
        if user.is_superuser:
            return Restaurant.objects.all()

        # بقیه فقط رستوران خودشون رو می‌بینن
        if user.restaurant:
            return Restaurant.objects.filter(id=user.restaurant.id)
        return Restaurant.objects.none()

    def perform_create(self, serializer):
        """
        فقط سوپریوزر می‌تواند رستوران جدید ایجاد کند.
        """
        user = self.request.user
        if not user.is_superuser :
            raise serializers.ValidationError("Only superusers can create restaurants.")
        serializer.save()



class RestaurantProfileViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantProfileSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrSuperuser]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return RestaurantProfile.objects.all()
        # فقط پروفایل مربوط به رستوران خودش
        return RestaurantProfile.objects.filter(restaurant=user.restaurant)

    def perform_create(self, serializer):
        user = self.request.user
        if not user.restaurant:
            raise serializers.ValidationError("You must be assigned to a restaurant to create a profile.")

        if RestaurantProfile.objects.filter(restaurant=user.restaurant).exists():
            raise serializers.ValidationError("You already have a restaurant profile.")

        serializer.save(restaurant=user.restaurant)
