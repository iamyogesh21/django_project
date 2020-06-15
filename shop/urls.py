
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="about"),
    path("shop/", views.shop, name="Shop"),
    path("contact/", views.contact, name="contact"),
    path("tracker/", views.tracker, name="tracker"),
    path("checkout/", views.checkout, name="Checkout"),
    path("search/", views.search, name="Search"),
    path("products/<int:id>", views.productView, name="Productview"),
    path("Cart/", views.Cart, name="Cart"),
]