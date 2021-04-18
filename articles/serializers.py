from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer): # 모델 폼과 유사하다는 점을 강조!

    class Meta:
        model = Article
        fields = ('id', 'title')


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)