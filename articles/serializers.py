from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer): # 모델 폼과 유사하다는 점을 강조!

    class Meta:
        model = Article
        fields = ('id', 'title')

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'