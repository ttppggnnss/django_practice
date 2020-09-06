from django.contrib import admin
from django.urls import path, include
from articles import views

app_name = 'accounts'

urlpatterns = [
    path('', views.movie_index),
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
]
