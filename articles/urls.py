from django.urls import path
from . import views

urlpatterns = [
    path('html/', views.article_html, name='article_html'),
    path('json-1/', views.article_json_1, name='json_1'),
    path('json-2/', views.article_json_2, name='json_2'),
]
