from django.urls import path, include
from issue import views

app_name='issue'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:issue_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:issue_pk>/reply/', views.reply, name='reply'),
    path('random/', views.random, name='random'),
]
