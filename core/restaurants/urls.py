from django.urls import path, include

app_name = "restaurants"

urlpatterns = [
    path("api/v1/", include("restaurants.api.v1.urls")),
]
