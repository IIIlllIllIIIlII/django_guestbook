from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class Article(models.Model):
    nickname = models.CharField(max_length=10)
    secretcode = models.CharField()
    content = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Article) 번호: {self.id} | 닉네임: {self.nickname} | 내용: {self.content} | 작성시간 (UTC): {self.datetime}"