from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('html/', views.article_html, name='article_html'),
    path('json-1/', views.article_json_1, name='json_1'),
    path('json-2/', views.article_json_2, name='json_2'),
    path('json-3/', views.article_json_3, name='json_3'),
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail, name='delete'),
    path('comments/', views.comment_list),
]
