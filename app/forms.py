from django import forms
from app.models import Post

class PostForm(forms.ModelForm): # HTML form을 통해 저장을 시도하는 값에 대한 유효성 검사 및 DB로의 저장
    class Meta:
        model = Post
        fields = '__all__'