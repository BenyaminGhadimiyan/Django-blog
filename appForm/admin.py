from django.contrib import admin
from appForm.models import Contact

class contactadmin(admin.ModelAdmin) :
    list_display=('name','email','subject','date')
    list_filter=('email',)
    search_fields=['name', 'message']

admin.site.register(Contact, contactadmin)