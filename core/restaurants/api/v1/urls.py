from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import RestaurantsViewSet, RestaurantProfileViewSet

router = DefaultRouter()
router.register('restaurants', RestaurantsViewSet, basename="restaurants")
router.register('restaurants_profile', RestaurantProfileViewSet, basename="restaurants_profile")

urlpatterns = [
    path('', include(router.urls))
]
