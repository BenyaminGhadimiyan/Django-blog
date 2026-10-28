from django.urls import path
from appForm.views import *

urlpatterns = [
    path('contact', contact_view,name='contact'),
]