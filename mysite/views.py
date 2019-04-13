from django.shortcuts import render
from .models import Contact
import requests, json


def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + ' & lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        context = {'joker': joke}
        return render(request, 'mysite/index.html', context)
    else:
        firstname = 'Ivan'
        lastname = 'Drew'
        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + ' & lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        context = {'joker': joke}
        return render(request, 'mysite/index.html', context)


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
