from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from app.models import Post

# Create your views here.
def index(request:HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    return render(request, 'app/index.html', {
        'post_list': qs,
    } ) # 세번째 인자에서 참조를 시켜줌