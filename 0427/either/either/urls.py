from django.contrib import admin
from django.urls import path, include
from issue import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('issue/', include('issue.urls')),
]
