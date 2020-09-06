from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('',views.read, name='index'),
    path('create/',views.create, name='create'),
    path('<int:review_pk>/',views.detail, name='detail'),
    path('<int:review_pk>/update/',views.update, name='update'),
    path('<int:review_pk>/delete/',views.delete, name='delete'),
    path('<int:review_pk>/comments/',views.c_create, name='c_create'),
    path('<int:review_pk>/comments/<int:comment_pk>/delete',views.c_delete, name='c_delete'),
]