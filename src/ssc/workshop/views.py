# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from workshop.models import Workshop


def index(request):
    return render(request, 'index.html')


def workshop(request):
    user = authenticate(username='peyman', password='peyman')
    login(request, user)
    ws = Workshop.objects.all()[0]
    return render(request, 'workshop.html', {'workshop': ws})


def logout_view(request):
    logout(request)
    return redirect('index')


@csrf_exempt
def register_view(request):
    if request.is_ajax():
        f = file('/Users/moreka/ce-list.txt')
        found = False
        needle = request.POST['studentID'] + ';' + request.POST['username']

        for line in f:
            if line.strip() == needle:
                found = True
                break
        if not found:
            return HttpResponse(u'{ "status": "fail", "error": "اکانت CE یا شماره دانشجویی غیر معتبر است." }')

    return HttpResponse("Salam")