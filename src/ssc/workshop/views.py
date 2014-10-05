# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from workshop.models import Workshop, SiteUser
from django.contrib.auth.models import User


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
            return HttpResponse(u'{ "status": "fail", "message": "اکانت CE یا شماره دانشجویی غیر معتبر است." }')

        user = User.objects.create_user(request.POST['username'],
                                        request.POST['mail'],
                                        request.POST['password'])

        user.save()

        siteuser = SiteUser()
        siteuser.user = user
        siteuser.studentID = request.POST['studentID']

        siteuser.save()
        user.save()

    return HttpResponse(u'{ "status": "success", "message": "ثبت نام موفقیت‌آمیز بود.<br> اکنون می‌توانید با این اکانت وارد شوید." }')


def login_view(request):
    if request.POST and request.is_ajax():
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print user, ',And,', username, password
        if user is None:
            return HttpResponse(u'{ "status": "fail", "message": "اطلاعات صحیح نیست." }')

        login(request, user)
        return HttpResponse(u'{ "status": "success", "message": "خوش آمدید" }')