from django.contrib import admin
from django.urls import path
from app import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', app_views.index),
    path('app/<int:pk>/', app_views.post_detail), # url 매핑 설정
]
