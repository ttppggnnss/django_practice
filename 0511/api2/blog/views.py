from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article, Comment
from .serializers import ArticleSerializer


@api_view(['GET']) # 반드시 써줘야 한다
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

@api_view(['POST'])
def create_article(request):
    serializer = ArticleSerializer()
    # if request.method == 'POST':
    #     form = ArticleForm(request.POST)
    print('wow')
