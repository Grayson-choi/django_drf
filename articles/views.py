from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ArticleListSerializer, ArticleSerializer


# 써드파티
from .models import Article # import 순서 강조해주기

# Create your views here.
def article_html(request):
    articles = get_list_or_404(Article) # article이 하나도 없다면 404 에러를 띄워준다. 여러개라 get_list_or_404를 써야함
    context = {
        'articles': articles
    }
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    articles = get_list_or_404(Article)
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
            }
        )
    return JsonResponse(articles_json, safe=False) # False로 설정하면 모든 개체를 serialization 할 수 있음 (그렇지 않으면 dict 인스턴스 만 허용됨)


def article_json_2(request):
    articles = get_list_or_404(Article)
    data = serializers.serialize(
        'json',
        articles
    )
    return HttpResponse(data, content_type='application/json') # content_type을 통해 body에 담긴 데이터가 어떤 것인지 알려준다.


# @api_view(['GET']) .accepted_renderer not set on Response 에러가 보인다면 데코레이터를 붙여야한다.
@api_view(['GET']) # 아무것도 안넣으면 GET임
def article_json_3(request):
    articles = get_list_or_404(Article)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def article_list(request):
    articles = get_list_or_404(Article)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk) # 1개니까 get_object_or_404
    serializer = ArticleSerializer(article)
    return Response(serializer.data)