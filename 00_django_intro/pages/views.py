from django.shortcuts import render

# Create your views here.
# 뷰에서 함수를 정의하는 경우 항상 첫번째 인자를 request로 정의한다.
def index(request):
    return render(request, 'index.html')

def hello(request):
    return render(request, 'hello.html')

def lotto(request):
    import random
    pick = sorted(random.sample(range(1,46),6))
    context={
        'pick':pick
    }
    return render(request, 'lotto.html', context)

def iam(request):
    iam_name='김세훈'
    context={
        'iam_name':iam_name
    }
    return render(request,'iam.html',context)

def lunch(request):
    menu=['돈까스','짜장면','먹지마','군만두','라면','김밥',]
    import random
    select_menu=random.choice(menu)
    context={
        "select_menu":select_menu, "menu":menu
    }
    return render(request, 'lunch.html', context)

def hi(request, name='이름이 뭐니?'):
    context={
        'name':name
    }
    return render(request, 'hi.html',context)

def add(request,a,b):
    result=a+b
    context={
        'result':result
    }
    return render(request, 'add.html',context)

def dinner(request, menu, people):
    context={
        'menu':menu, 'people':people,
    }
    return render(request,'dinner.html',context)

def posts(request,number):
    context={
        'number':number,
        'replies':[11111,222222,3333333,],
        'no_replies':[],
        'content':'Life is short',
        'user':'eric',
    }
    return render(request, 'posts.html',context)