from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.conf.urls import url
from . import views

urlpatterns = [
    #主页
    url(r'^$', views.index, name='index'),

    #显示所有电影页面
    url(r'^movies/$', views.movies, name='movies'),

    #每部电影的详细页面
    url(r'^movies/(?P<movie_id>\d+)/$', views.movie, name='movie'),

    #用于对用户添加新电影
    url(r'^new_movie/$', views.new_movie, name='new_movie'),

    #用于添加新评论的页面
    url(r'^new_comment/(?P<movie_id>\d+)/$', views.new_comment, name='new_comment'),

    #用于编辑评论的页面
    url(r'^edit_comment/(?P<comment_id>\d+)/$', views.edit_comment, name='edit_comment'),
]

urlpatterns += staticfiles_urlpatterns()
