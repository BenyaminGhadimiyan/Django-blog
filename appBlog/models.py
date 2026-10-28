from django.db import models
from django.contrib.auth.models import User

class Category(models.Model) :
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Post(models.Model) :
    image=models.ImageField(upload_to='blog/',default='blog/1.jpg')
    title=models.CharField(max_length=255)
    author=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    category=models.ManyToManyField(Category)
    content=models.TextField()
    conted_viwes=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    published_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self) :
        return f"{self.title} - {self.id}"

class Comment(models.Model) :
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()
    approved=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now=True)
    updated_date=models.DateTimeField(auto_now=True)
    class Meta :
        ordering=['-created_date']

    def __str__(self):
         return self.name




