from rest_framework import serializers
from core.models import *

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title','content','category')


class SubscriberSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = Subscriber
        fields = ['email',]