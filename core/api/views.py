from rest_framework import generics
from core.models import News
from .serializers import NewsSerializer

class NewsListAPIView(generics.CreateAPIView):
    queryset=News.objects.all()
    serializer_class=NewsSerializer
     