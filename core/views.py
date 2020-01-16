from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.views.generic import View
from django.conf import settings
    

# Create your views here.

#add configurations for smtp server
def index(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)    
        
        if form.is_valid():
            name = form.cleaned_data['name']

            subject = form.cleaned_data['subject']
            from_email = settings.EMAIL_HOST_USER
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['alexmwaura43@gmail.com'],html_message="html_message")
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    # send_mail(subject, message, from_email, ['alexmwaura43@gmail.com'],html_message="html_message")
    return render(request, "index.html", {'form': form})


# if request.method == 'POST':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']

#             subject = form.cleaned_data['subject']
#             from_email = settings.EMAIL_HOST_USER
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['alexmwaura43@gmail.com'],html_message="html_message")
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')


def single(request):
	return render(request, 'blog-single.html')	




def successView(request):
    return HttpResponse('Success! Thank you for your message.')