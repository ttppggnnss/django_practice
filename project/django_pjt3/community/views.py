from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.
def read(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews':reviews,
    }
    return render(request, 'community/review_list.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.hitcount=0
            review.user = request.user
            review.save()
            messages.info(request, '글이 작성되었습니다.')
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form':form,
    }
    return render(request, 'community/form.html', context)

def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    review.hitcount+=1
    review.save()
    form = CommentForm()
    context = {
        'review':review,
        'form':form,
    }
    return render(request, 'community/review_detail.html', context)

@require_POST
@login_required
def c_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        messages.info(request, '댓글이 작성되었습니다.')
    return redirect('community:detail',review.pk)

@login_required
def c_delete(request,review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    messages.info(request, '댓글이 삭제되었습니다.')
    return redirect('community:detail', review_pk)

@login_required
def update(request, review_pk):
    review = get_object_or_404(Review, id=review_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review=form.save()
            messages.info(request, '글이 수정되었습니다.')
            return redirect('community:detail', review.id)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
        'review':review,
    }
    return render(request,'community/form.html', context)

@require_POST
def delete(request, review_pk):
    if request.user == get_object_or_404(User, id=rget_object_or_404(Review, id=review_pk).user_id):
        review = get_object_or_404(Review, id=review_pk)
        review.delete()
        messages.info(request, '글이 삭제되었습니다.')
    return redirect('community:index')