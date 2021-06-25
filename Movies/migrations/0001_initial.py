# Generated by Django 3.2.4 on 2021-06-14 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('introduction', models.TextField(verbose_name='电影简介')),
                ('added_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('com_num', models.IntegerField(verbose_name='评论数')),
                ('grade', models.IntegerField(verbose_name='评分')),
            ],
            options={
                'verbose_name': '电影信息',
                'verbose_name_plural': '电影信息',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='评论详情')),
                ('added_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movies.movie', verbose_name='对应电影')),
            ],
            options={
                'verbose_name': '电影评论',
                'verbose_name_plural': '电影评论',
            },
        ),
    ]
