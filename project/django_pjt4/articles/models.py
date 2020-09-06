from django.db import models
from django.conf import settings

class Movie(models.Model):
    movie_title = models.CharField(max_length = 100)
    movie_poster = models.TextField()

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete = models.CASCADE)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    hitcount = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                            related_name='like_reviews')

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    review = models.ForeignKey(Review,related_name='comments', on_delete = models.CASCADE)
    content = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
