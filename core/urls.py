from django.urls import path
from core.views import (
    home,
    contact,
    products,
    product_single,
    news,
    news_single,
    about,
    search,
)


urlpatterns = [
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    path("shop/", products, name="products"),
    path("blog/", news, name="news"),
    path("product/<int:id>/", product_single, name="product_single"),
    path("news/<int:id>/", news_single, name="news_single"),
    path("search/", search, name="search"),
]
