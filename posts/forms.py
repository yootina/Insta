from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'like_users', )


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'cols': '20', 'rows': '1', 'placeholder': '댓글 달기...', 'style':"border-color: white;"},
        )
    )
    class Meta:
        model = Comment
        exclude = ('user', 'post', )