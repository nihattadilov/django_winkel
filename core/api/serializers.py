from rest_framework import serializers
from core.models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title','content','category')
