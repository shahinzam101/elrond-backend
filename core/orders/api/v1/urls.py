from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import OrderItemViewSet, OrderViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet, basename="orders")
router.register('order_items', OrderItemViewSet, basename="order_items")

urlpatterns = [
    path('', include(router.urls))
]
