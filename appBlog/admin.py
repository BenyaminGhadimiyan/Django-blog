from django.contrib import admin
from appBlog.models import Post,Category,Comment

class postadmin(admin.ModelAdmin) :
    list_display=('title','author','conted_viwes','status','published_date','created_date')
    list_filter=('status',)
    search_fields=['title', 'content']

class postComment(admin.ModelAdmin) :
    date_hierarchy='created_date'
    list_display=('name','post','approved','created_date')
    list_filter=['name']
    ordering=['created_date']
    search_fields=['name', 'post']

admin.site.register(Post,postadmin)
admin.site.register(Category)
admin.site.register(Comment,postComment)