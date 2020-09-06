from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from django.http.response import JsonResponse, HttpResponse


from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Article
from .serializers import ArticleSerializer

# Nogada 방식
# 직관적으로
# field 30개 면 어떻게 하려고
@require_GET
def article_list_json_1(request):
    articles = Article.objects.all()

    data = []
    for article in articles:
        data.append({
            "article_id": article.id,
            "title": article.title,
            "content" :article.content,
            "created_at":article.created_at,
            "updated_at":article.updated_at,
        })

    return JsonResponse(data, safe=False)


# django core serializer
# 이것도 다시 볼 일 없음
@require_GET
def article_list_json_2(request):
    from django.core import serializers

    articles = Article.objects.all()
    data = serializers.serialize('json',articles)
    # 데이터를 덤프 할 때 쓰는 것

    # return JsonResponse(data, safe=False)
    return HttpResponse(data, content_type='application/json')


# rest framework
# @require_GET
# @require_http_methods(['GET','POST'])
# 과 유사하게
@api_view(['GET'])
def article_list_json_3(request):
    articles = Article.objects.all()
    # form = ArticleForm()
    serializer = ArticleSerializer(articles, many=True)
    # many=True 는 쿼리셋일 떄 옵션 주는 것

    # rest framework 의 serializer 를 리턴하려면 res framework 의 response 의 Response 써야 한다

    return Response(serializer.data)