from rest_framework import viewsets, filters, serializers
from restaurants.models import Restaurant, RestaurantProfile
from .serializers import RestaurantProfileSerializer, RestaurantSerializer
from .permissions import IsOwnerOrSuperuser

class RestaurantsViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    search_fields = ["name",]
    filter_backends = [filters.SearchFilter]



class RestaurantProfileViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantProfileSerializer
    search_fields = ["restaurant__name"]
    permission_classes = [IsOwnerOrSuperuser]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return RestaurantProfile.objects.all()
        return RestaurantProfile.objects.filter(restaurant__user=user)  # فرض بر اینکه فیلد user در مدل Restaurant هست

    def perform_create(self, serializer):
        user = self.request.user

        if not user.is_superuser:
            # جلوگیری از ساخت چند پروفایل توسط یک کاربر
            if RestaurantProfile.objects.filter(restaurant__user=user).exists():
                raise serializers.ValidationError("You already have a restaurant profile.")

        serializer.save()