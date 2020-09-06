from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.movie_index, name='movie_index'),
    path('<int:movie_pk>/', views.reviews_index, name='reviews_index'),
    path('<int:movie_pk>/<int:review_pk>', views.review_detail, name='review_detail'),
    path('<int:movie_pk>/create/', views.create, name='create'),
    path('<int:movie_pk>/<int:review_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/<int:review_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/<int:review_pk>/c_comment/', views.c_comment, name='c_comment'),
    path('<int:movie_pk>/<int:review_pk>/<int:comment_pk>/d_comment/', views.d_comment, name='d_comment'),
    path('<int:movie_pk>/<int:review_pk>/like/', views.like, name='like'),
]
