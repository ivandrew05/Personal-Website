from django.shortcuts import render
from .models import Contact
import requests, json


def index(request):
    return render(request, 'mysite/index.html')


def portfolio(request):
    return render(request, 'mysite/portfolio.html')


def contact(request):
    if request.method == 'POST':
        email_received = request.POST.get('email')
        subject_received = request.POST.get('subject')
        message_received = request.POST.get('message')

        c = Contact(email=email_received, subject=subject_received, message=message_received)
        c.save()
        return render(request, 'mysite/thank.html')
    else:
        return render(request, 'mysite/contact.html')


def carousel1(request):
    return render(request, 'mysite/carousel1.html')


def carousel2(request):
    return render(request, 'mysite/carousel2.html')
    
