from django.urls import path
from . import views


urlpatterns = [
    path('api/products', views.handle_products),
]