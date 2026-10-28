from django.shortcuts import render,get_object_or_404
from appBlog.models import Post,Comment
from appBlog.forms import Commentform
from django.contrib import messages

def bloghome_view(request) :
    Posts=Post.objects.filter(status=1)
    context={'posts': Posts}
    return render(request,'Blog/blog-home.html',context)

def blogsingle_view(request,pid) :
    if request.method=='POST' :
        form=Commentform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'کامنت ثبت شد')
        else :
              messages.add_message(request,messages.SUCCESS,'کامنت ثبت نشد')
    posts=Post.objects.filter(status=True)
    post=get_object_or_404(Post, pk=pid, status=1)
    comments=Comment.objects.filter(post=post.id,approved=True)
    form=Commentform()
    context={'post': post , 'comments':comments , 'form':form}
    return render(request,'Blog/blog-single.html',context)


