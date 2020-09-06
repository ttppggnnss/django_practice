from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST

from .models import Issue, Reply
from .forms import IssueForm, ReplyForm

def index(request):
    issues = Issue.objects.order_by('-pk')
    context = {
        'issues':issues,
    }
    return render(request, 'issue/index.html', context)

def detail(request, issue_pk):
    issue = get_object_or_404(Issue, pk=issue_pk)
    form = ReplyForm()
    context = {
        'issue':issue,
        'form':form,
    }
    return render(request, 'issue/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.hitcountA=0
            issue.hitcountB=0
            issue.save()
            messages.info(request, '이슈가 작성되었습니다.')
            return redirect('issue:detail', issue.pk)
    else:
        form = IssueForm()
    context = {
        'form':form,
    }
    return render(request, 'issue/form.html', context)

def reply(request,issue_pk):
    issue = get_object_or_404(Issue, pk=issue_pk)
    form = ReplyForm(request.POST)
    if form.is_valid():
        reply = form.save(commit=False)
        if reply.pick=='A':
            issue.hitcountA+=1
        else:
            issue.hitcountB+=1
        issue.save()
        reply.issue = issue
        reply.save()
        messages.info(request, '의견이 반영되었습니다.')
    return redirect('issue:detail', issue.pk)

def random(request):
    issues=Issue.objects.all()
    import random
    issue=random.choice(issues)
    return redirect('issue:detail',issue.pk)