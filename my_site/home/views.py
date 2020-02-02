from django.shortcuts import render


def index(request):
    return render(request, 'home/main.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')
