from django import template
from appBlog.models import Post,Comment

register=template.Library()

@register.simple_tag(name='comments_count') 
def function(pid):
    post=Post.objects.get(pk=pid)
    return Comment.objects.filter(post=post.id,approved=True).count()