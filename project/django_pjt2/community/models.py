from django.db import models

# Create your models here.
class Review(models.Model):
    movie_title = models.CharField(max_length=30)
    rank = models.DecimalField(max_digits=5, decimal_places=1)
    title = models.CharField(max_length=100)
    reviewer = models.CharField(max_length=10)
    password = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hitcount = models.IntegerField()