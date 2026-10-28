from django.urls import path
from appMFT.views import *

urlpatterns = [
    path('', index_view,name='index'),
    path('about', about_view,name='about'),
    path('elements', elements_view,name='elements'),
]