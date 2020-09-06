from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request,'home.html')

def dinner(request):
    menu = ['피자', '치킨', '짜장면', '초밥']
    din = random.choice(menu)
    return render(request, 'dinner.html', {'din':din})

def lotto(request):
    numbers=random.sample(range(1,46),6)
    numbers=sorted(numbers)
    numbers=' '.join(map(str,numbers))
    return render(request,'lotto.html',{'lotto':numbers})


