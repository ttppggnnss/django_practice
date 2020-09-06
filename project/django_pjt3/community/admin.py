from django.contrib import admin
from .models import Review, Comment

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'movie_title', 'content', 'created_at', 'updated_at', )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', )

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)