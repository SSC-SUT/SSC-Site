from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def workshop(request):
    return render(request, 'workshop.html')