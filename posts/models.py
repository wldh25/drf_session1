# django model setting
from django.db import models
from django.contrib.auth import get_user_model

from django.conf import settings

# User = get_user_model()

class Post(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    content = models.TextField('내용')
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    view_count = models.IntegerField('조회수', default=0)
    writer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)


class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    post = models.ForeignKey(to="Post", on_delete=models.CASCADE)
    writer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)