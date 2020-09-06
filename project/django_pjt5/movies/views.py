from datetime import datetime, date
import random

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from .models import Movie, Genre

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies': movies,
        'page_obj': page_obj,
    }
    return render(request, 'movies/index.html', context)

@login_required
def like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(id=request.user.pk).exists():
        movie.like_users.remove(request.user)
        liked=False
    else:
        movie.like_users.add(request.user)
        liked=True
    context = {
        'liked': liked,
        'count': movie.like_users.count(),
    }
    return JsonResponse(context)


@login_required
def recommend(request):
    day = datetime.today().day
    day=str(day)
    if len(day)==1:
        day='0'+day
    movies = Movie.objects.filter(release_date__endswith=day)
    if len(movies) >= 10:
        movies = random.sample(list(movies), 10)
    context = {
        'movies': movies,
        'day':day,
    }
    return render(request, 'movies/recommend.html', context)

def genre(request, genre_pk):

    movies = Movie.objects.filter(genres=genre_pk)
    genre = Genre.objects.get(pk=genre_pk)

    paginator = Paginator(movies, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies': movies,
        'page_obj': page_obj,
        'genre':genre.name
    }
    return render(request, 'movies/genre.html', context)
