from django.urls import path
from .views import *

urlpatterns = [
    path('productss/', NewsListAPIView.as_view(), name='product-list'),
    path('subscriber/', SubsciberApiView.as_view(), name='subscriber'),
    # Add other URL patterns as needed
]
