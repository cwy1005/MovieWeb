from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'introduction', 'release_time', 'com_num','grade']
        labels = {'title': '', 'introduction': '', 'release_time': '', 'com_num':'','grade': ''}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}
