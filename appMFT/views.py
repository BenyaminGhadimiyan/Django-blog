from django.shortcuts import render

def index_view(request) :
    return render(request,'pages/index.html')

def about_view(request) :
    return render(request,'pages/about.html')

def elements_view(request) :
    return render(request,'pages/elements.html')



