from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Movie, Review, Comment
from .forms import ReviewForm, CommentForm

def movie_index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request, 'articles/movie_list.html', context)

def reviews_index(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie':movie,
    }
    return render(request, 'articles/review_list.html', context)

def review_detail(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm()
    context = {
        'movie':movie,
        'review':review,
        'form':form,
    }
    return render(request, 'articles/review_detail.html', context)

@login_required
def create(request, movie_pk):
    movie=get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.hitcount=0
            review.user = request.user
            review.movie_id=movie_pk
            review.save()
            messages.info(request, '글이 작성되었습니다.')
            return redirect('articles:review_detail', movie.pk, review.pk)
    else:
        form = ReviewForm()
    context = {
        'movie':movie,
        'form':form,
    }
    return render(request, 'articles/form.html', context)

@login_required
def update(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, id=movie_pk)
    review = get_object_or_404(Review, id=review_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review=form.save()
            review.movie_id=movie_pk
            messages.info(request, '글이 수정되었습니다.')
            return redirect('articles:review_detail', movie.pk, review.id)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
        'review':review,
        'movie':movie,
    }
    return render(request,'articles/form.html', context)

@login_required
def delete(request, movie_pk, review_pk):
    User = get_user_model()
    if request.user == get_object_or_404(User, id=get_object_or_404(Review, id=review_pk).user_id):
        review = get_object_or_404(Review, id=review_pk)
        review.delete()
        messages.info(request, '글이 삭제되었습니다.')
    return redirect('articles:reviews_index', movie_pk)



@require_POST
@login_required
def c_comment(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        messages.info(request, '댓글이 작성되었습니다.')
    return redirect('articles:review_detail',movie_pk, review_pk)

@login_required
def d_comment(request, movie_pk, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    messages.info(request, '댓글이 삭제되었습니다.')
    return redirect('articles:review_detail', movie_pk, review_pk)

@login_required
def like(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(id=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('articles:review_detail', movie_pk, review_pk)