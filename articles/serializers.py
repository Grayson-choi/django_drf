from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer): # 모델 폼과 유사하다는 점을 강조!

    class Meta:
        model = Article
        fields = ('id', 'title')




class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    comment_first = serializers.CharField(source='comment_set.first', read_only=True) #3
    # comment_first = CommentSerializer(source='comment_set.first', read_only=True)
    comment_filter = serializers.SerializerMethodField('less_10')

    def less_10(self, article):
        print(article) # views.py article_detail에서 들고온 article instance.
        qs = Comment.objects.filter(pk__lte=15, article=article)
        serializer = CommentSerializer(instance=qs, many=True)
        return serializer.data
    

    class Meta:
        model = Article
        fields = '__all__'

