from django.db import models

# Create your models here.

class Article(models.Model):
    nickname = models.CharField(max_length=10)
    content = models.TextField(default="")
    datetime = models.DateTimeField(auto_now_add=True)