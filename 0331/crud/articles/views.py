from django.shortcuts import render,redirect

# Create your views here.
def community(request):
    from . models import Article
    articles=Article.objects.all()
    context={
        'articles':articles,
    }
    return render(request,'articles/community.html',context)

def community_complete(request):
    from . models import Article

    article = Article()
    title=request.GET.get('title')
    content=request.GET.get('content')
    article.title=title
    article.content=content
    article.save()

    articles=Article.objects.all()
    context={
        'articles':articles,
    }
    return redirect(f'/articles/detail/{article.id}')
    # return render(request,'articles/complete.html',context)

def ping(request):
    context={
    }
    return render(request,'articles/ping.html',context)

def pong(request):
    data = request.GET.get('data')
    context={
        'data':data
    }
    return render(request,'articles/pong.html',context)

def detail(request,article_id):
    from . models import Article
    article=Article.objects.get(id=article_id)
    context={
        'article':article,
    }
    return render(request,'articles/detail.html', context)

def new(request):
    context={

    }
    return render(request,'articles/new.html',context)

def create(request):
    from .models import Article

    article=Article()
    title=request.GET.get('title')
    title=title[:20]
    content=request.GET.get('content')
    article.title=title
    article.content=content
    article.save()
    # article2=Article(title=title, content=content+'b').save()
    # article3=Article(title,content+'c').save()
    # article4=Article.objects.create(title=title,content=content+'d').save()
    context={
    }
    return render(request,'articles/create.html',context)

def index(request):
    from .models import Article
    articles=Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request,'articles/index.html',context)