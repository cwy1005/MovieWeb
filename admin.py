from django.contrib import admin
from Movies.models import Movie, Comment
# Register your models here.

admin.site.register(Movie)
admin.site.register(Comment)