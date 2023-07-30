from django.contrib import admin
from django.urls import path, include
from app import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', app_views.index),
    path('app/<int:pk>/', app_views.post_detail), # url 매핑 설정
    path('app/new/', app_views.post_new),
    path('accounts/', include('accounts.urls'))
]
