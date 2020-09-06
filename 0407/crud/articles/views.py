from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_POST

# Create your views here.
def read(request):
    articles=Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request,'articles/read.html',context)

# @require_POST
def create(request):
    if request.method=='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            article=form.save()
            return redirect('articles:detail',article.id)
    else:
        form=ArticleForm()
    context={
        'form':form
    }
    return render(request,'articles/create.html',context)

def detail(request, id):
    article=get_object_or_404(Article,id=id)
    context={
        'article':article
    }
    return render(request,'articles/detail.html',context)

# @require_POST
def update(request, id):
    article=get_object_or_404(Article,id=id)
    # if request.method == 'POST':
    #     form = ArticleForm(request.POST, instance=article)
    #     if form.is_valid():
    #         article = form.save()
    #         return redirect('articles:detail',article.id)
    if request.method=='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            article.title=form.cleaned_data['title']
            article.content=form.cleaned_data['content']
            article.save()
            return redirect('articles:detail',article.id)
    else:
        form=ArticleForm(instance=article)
    context={
        'form':form,
        'article':article
    }
    return render(request,'articles/update.html',context)

def delete(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()
    return redirect('articles:index')