from django.shortcuts import render
from appForm.forms import ContactForm
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'saved👌')
        else:
            messages.add_message(request, messages.ERROR, 'Dont saved❌')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})