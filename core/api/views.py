from rest_framework import generics
from core.models import *
from .serializers import *
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class NewsListAPIView(generics.CreateAPIView):
    queryset=News.objects.all()
    serializer_class=NewsSerializer
     
     
class SubsciberApiView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = SubscriberSerializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)