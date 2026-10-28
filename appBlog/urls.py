from django.urls import path
from appBlog.views import *

app_name='Blog'

urlpatterns = [
    path('Blog/',bloghome_view,name='index'),
    path('<int:pid>',blogsingle_view,name='single'),
]
