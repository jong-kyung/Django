from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import CreateView
from app.models import Post
from app.forms import PostForm

# Create your views here.
@login_required
def index(request:HttpRequest) -> HttpResponse:
    # if not request.user.is_authenticated:
    #     return redirect('/accounts/login')
    
    qs = Post.objects.all()
    return render(request, 'app/index.html', {
        'post_list': qs,
    } ) # 세번째 인자에서 참조를 시켜줌

def post_detail(request: HttpRequest, pk :int) -> HttpResponse:
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post,pk=pk) # 해당 페이지가 없으면 404로 뜨게해줌
    return render(request, 'app/post_detail.html',{
        'post' : post,
    })

post_new = CreateView.as_view(
    model = Post,
    form_class = PostForm,
    success_url = '/app/'
)