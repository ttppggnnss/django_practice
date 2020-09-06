from django.contrib import admin

from .models import Movie, Review, Comment

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_title', 'movie_poster', )

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'rank', 'content', )

class CommentAdmin(admin.ModelAdmin):
    list_display =('user', 'content', )

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
