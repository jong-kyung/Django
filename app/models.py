from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100) # 길이제한이 있는 문자열
    content = models.TextField()
    tag_set = models.ManyToManyField('Tag', blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # CASCADE 부모가 삭제되면 부모에 포함된 자식들도 삭제한다
    mesaage = models.TextField()

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Article(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    currented_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)