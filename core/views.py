from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def signin(request):
    return render(request, 'signin.html')