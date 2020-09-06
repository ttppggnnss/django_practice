from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def read(request):
    articles=Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request,'articles/read.html',context)

def new(request):
    return render(request,'articles/new.html')

def create(request):
    article=Article()
    title=request.POST.get('title')
    title=title[:20]
    content=request.POST.get('content')
    article.title=title
    article.content=content
    article.save()
    return redirect(f'/articles/{article.id}')

def detail(request, id):
    article=Article.objects.get(id=id)
    context={
        'article':article
    }
    return render(request,'articles/detail.html',context)

def edit(request, id):
    article=Article.objects.get(id=id)
    context={
        'article':article
    }
    return render(request,'articles/edit.html',context)

def update(request,id):
    article=Article.objects.get(id=id)
    title=request.POST.get('title')
    title=title[:20]
    content=request.POST.get('content')
    article.title=title
    article.content=content
    article.save()
    return redirect('articles:detail',article.id)

def delete(request,id):
    article=Article.objects.get(id=id)
    article.delete()
    return redirect('articles:index')