from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100) # 길이제한이 있는 문자열
    content = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    currented_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)