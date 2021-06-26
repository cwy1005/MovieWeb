from django.shortcuts import render
from .models import Movie, Comment
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import MovieForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    """电影网站的主页"""
    return render(request, 'Movies/index.html')

def movies(request):
    """显示所有的电影"""
    movies = Movie.objects.order_by('-grade')
    context = {'movies': movies}
    return render(request, 'Movies/movies.html', context)

@login_required
def movie(request, movie_id):
    """显示每部电影的详细信息"""
    movie = Movie.objects.get(id=movie_id)
    comments = movie.comment_set.order_by('-added_time')
    context = {'movie': movie, 'comments': comments}
    return render(request, 'Movies/movie.html', context)

@login_required
def new_movie(request):
    """添加新电影"""
    if request.user.username != 'cwy':           #只有超级用户可以添加新电影
        raise Http404
    else:
        if request.method != 'POST':
            #未提交数据：创建一个新表单
            form = MovieForm()
        else:
            #POST提交的数据，对数据进行处理
            form = MovieForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('Movies:movies'))

    context = {'form': form}
    return render(request, 'Movies/new_movie.html', context)

@login_required
def new_comment(request, movie_id):
    """在特定电影中添加新评论"""
    movie = Movie.objects.get(id = movie_id)

    if request.method != 'POST':
        #未提交数据，创建一个新表单
        form = CommentForm()
    else:
        #POST提交的数据，对数据进行处理
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.owner = request.user
            new_comment.movie = movie
            new_comment.save()
            movie.com_num += 1
            return HttpResponseRedirect(reverse('Movies:movie', args=[movie.id]))
    context = {'movie': movie, 'form': form}
    return render(request, 'Movies/new_comment.html', context)

@login_required
def edit_comment(request,comment_id):
    """编辑既有评论"""
    comment = Comment.objects.get(id=comment_id)
    movie = comment.movie
    if comment.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #初次请求，使用当前条目填充表单
        form = CommentForm(instance = comment)
    else:
        #post提交的数据，对数据进行处理
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Movies:movie',
                                        args=[movie.id]))
    context = {'comment':comment, 'movie':movie, 'form':form}
    return render(request,'Movies/edit_comment.html', context)
