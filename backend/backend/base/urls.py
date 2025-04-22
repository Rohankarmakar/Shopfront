from django.urls import path

from base.views import check_health, get_or_create_products, get_product

urlpatterns = [
    path("health/", check_health, name="health-check"),
    path("products/<int:pk>/", get_product, name="get-product"),
    path("products/", get_or_create_products, name="get-create-products"),
]
