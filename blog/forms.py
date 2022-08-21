from django import forms

from .models import Post

#Formulario para crear un post 
class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','content')