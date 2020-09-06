from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout

from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:movie_index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:movie_index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:movie_index')

@login_required
def profile(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    context = {
        'user': user
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    if user != request.user:
        if user.followers.filter(username=request.user.username).exists():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
    return redirect('accounts:profile', username)

@login_required
def delete(request):
    request.user.delete()
    messages.info(request, '회원탈퇴 되었습니다.')
    return redirect('articles:movie_index')