from django.urls import path
from .views import NewsListAPIView

urlpatterns = [
    path('productss/', NewsListAPIView.as_view(), name='product-list'),
    # Add other URL patterns as needed
]
