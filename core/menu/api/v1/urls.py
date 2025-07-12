from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import MenuItemViewSet, CategoryViewSet

router = DefaultRouter()
router.register('menu', MenuItemViewSet, basename="menu")
router.register('categories', CategoryViewSet, basename="categories")

urlpatterns = [
    path('', include(router.urls))
]
