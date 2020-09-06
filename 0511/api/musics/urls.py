from django.urls import path
from . import views

app_name = 'musics'

urlpatterns = [
    path('artists/', views.artists, name='artists'),
    path('artists/<int:artist_pk>/', views.artist_detail, name='artist_detail'),
    path('musics/', views.music, name='musics'),
    path('musics/<int:music_pk>/', views.music_detail, name='music_detail'),
    path('musics/<int:music_pk>/comments/', views.comment_create),
    path('comments/<int:comment_pk>/',views.comment_pd),
]
