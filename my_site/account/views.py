from django.shortcuts import render

# Create views.

def signin(request):
    return render(request, 'account/signin.html')

def signup(request):
    return render(request, 'account/signup.html')

def signout(request):
    return render(request, 'account/signout.html')