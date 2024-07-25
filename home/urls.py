from django.urls import path
from .views import home, details, about, add_product, register, add_to_cart, cart, remove_item, checkout

urlpatterns = [
    path("", home, name="home"),
    path("about", about, name="about"),
    path("product/<id>", details, name="product_details"),
    path("add_product", add_product, name="add_product"),
    path("add/<id>", add_to_cart, name="add_to_cart"),
    path("register", register, name="register"),
    path("cart", cart, name="view_cart"),
    path("remove_item/<id>", remove_item, name="remove_item"),
    path("checkout", checkout, name="checkout")
]