from django import forms
from .models import Comment, Post


class CommmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # nếu có author, không thì hiển thị none
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        # overwrite save function of model
        # if commit = false then it doesn't save in database
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.save()  # save to database

    class Meta:
        model = Comment
        fields = ['body']


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # nếu có author, không thì hiển thị none
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        # overwrite save function of model
        # if commit = false then it doesn't save in database
        post = super().save(commit=False)
        post.author = self.author
        post.save()  # save to database

    class Meta:
        model = Post
        fields = ['title', 'body', 'image']
