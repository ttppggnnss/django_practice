from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)

class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='musics')
    title = models.CharField(max_length=100)

class Comment(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()