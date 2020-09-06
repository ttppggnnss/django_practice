from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/comments/', views.comments, name='comments'),
    path('<int:article_pk>/c_delete/<int:comment_pk>',views.c_delete, name='c_delete'),
]