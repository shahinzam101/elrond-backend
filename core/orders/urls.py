from django.urls import include, path 


app_name = 'orders'

urlpatterns = [
    path("api/v1/", include("orders.api.v1.urls")),
]

