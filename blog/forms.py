from django.forms import ModelForm

from blog.models import BlogPost


class BlogPostCreate(ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'preview', 'is_published',)
