# models.py를 기반을 만들기 때문에 Models.py 와 같은 위치에 만든다

from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'contents', 'image']