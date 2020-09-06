from django.urls import path
from . import views

urlpatterns = [
    path('community/',views.community),
    path('complete/',views.community_complete),
    path('ping/', views.ping),
    path('pong/', views.pong),
    path('detail/<int:article_id>/',views.detail),
    path('new/', views.new),
    path('create/',views.create),
    path('',views.index),
]
