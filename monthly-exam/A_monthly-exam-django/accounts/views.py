from django.shortcuts import render
# 각 문제를 해결하기 위하여 필요한 import문은 이곳에 작성합니다.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout


def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    if request.method == 'POST': # POST 방식일 때
        form = UserCreationForm(request.POST) # UserCreationForm 활용
        if form.is_valid(): # 유효성 검사
            form.save() # 저장
            return redirect('accounts:index') # accounts 경로로 리다이렉트
        else:
            messages.info(request, '정확히 입력해주세요') # valid 안할 때 메세지

    else: # GET 방식일 때
        form = UserCreationForm() # UserCreationForm 활용
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context) # accounts/form.html 렌더

def login(request):
    if request.user.is_authenticated: # 로그인 되어 있는 경우
        return redirect('accounts:index')

    if request.method == 'POST': # POST 방식일 때
        form = AuthenticationForm(request, request.POST) # AuthenticationForm 활용
        if form.is_valid(): # 유효성 검사
            auth_login(request, form.get_user()) # 세션에 로그인
            return redirect('accounts:index') # 로그인 된 후 accounts 경로로 리다이렉트
    else:
        form = AuthenticationForm() # AuthenticationForm 활용
    context = {
        'form' : form
    }
    return render(request, 'accounts/form.html', context) # accounts/form.html 렌더

@login_required # 로그인 되어 있는 경우에
def logout(request):
    auth_logout(request) # 세션에서 로그아웃
    return redirect('accounts:index') # accounts 경로로 리다이렉트