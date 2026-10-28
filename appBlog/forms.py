from django import forms
from appBlog.models import Comment

class Commentform(forms.ModelForm) :

    class Meta :
        model= Comment
        fields=['post','name','email','subject','message']