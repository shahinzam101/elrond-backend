from django.urls import include, path 


app_name = 'menu'

urlpatterns = [
    path("api/v1", include("menu.api.v1.urls")),
]

