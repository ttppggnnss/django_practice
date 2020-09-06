from django.contrib import admin
from .models import Artist, Music, Comment

# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)

class MusicAdmin(admin.ModelAdmin):
    list_display = ('artist', 'title',)

class CommentAdmin(admin.ModelAdmin):
    list_display =('music', 'content',)

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(Comment, CommentAdmin)