from django.shortcuts import render, get_list_or_404
from django.http.response import JsonResponse
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