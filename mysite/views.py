from django.shortcuts import render
from .models import Contact
import requests
import json


def index(request):
    return render(request, 'mysite/index.html')


def portfolio(request):
    return render(request, 'mysite/portfolio.html')


def contact(request):
    if request.method == 'POST':
        email_received = request.POST.get('email')
        subject_received = request.POST.get('subject')
        message_received = request.POST.get('message')

        c = Contact(email=email_received, subject=subject_received,
                    message=message_received)
        c.save()
        return render(request, 'mysite/thank.html')
    else:
        return render(request, 'mysite/contact.html')


def carousel1(request):
    return render(request, 'mysite/carousel1.html')


def carousel2(request):
    return render(request, 'mysite/carousel2.html')


def video1(request):
    return render(request, 'mysite/video1.html')


def video2(request):
    return render(request, 'mysite/video2.html')


def video3(request):
    return render(request, 'mysite/video3.html')


def video4(request):
    return render(request, 'mysite/video4.html')


def video5(request):
    return render(request, 'mysite/video5.html')


def video6(request):
    return render(request, 'mysite/video6.html')


def album2(request):
    return render(request, 'mysite/album2.html')
