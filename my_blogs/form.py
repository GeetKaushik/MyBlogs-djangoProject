from .models import Blog_Category, Blog_Post
from django.forms import ModelForm
from ckeditor.fields import RichTextField

class Blog_Form(ModelForm):
    class Meta:
        model = Blog_Category
        fields="__all__"  


class Blogpost_form(ModelForm):
    class Meta:
        model = Blog_Post
        fields = "__all__"


# Everything here
        # fiels?, model, etc