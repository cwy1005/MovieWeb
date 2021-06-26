from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    introduction = models.TextField(verbose_name='电影简介')
    release_time = models.DateField(default=datetime.now, verbose_name='上映时间')
    added_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    com_num = models.IntegerField(verbose_name='评论数')
    grade = models.IntegerField(verbose_name='评分')

    class Meta:
        verbose_name = '电影信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE, verbose_name='对应电影')
    text = models.TextField(verbose_name='评论详情')
    added_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '电影评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text[:50] + "..."

