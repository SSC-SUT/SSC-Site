# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.utils import IntegrityError
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from workshop.models import Workshop, SiteUser
from django.contrib.auth.models import User


def index(request):
    return render(request, 'indexp.html')


def workshop(request):
    ws = Workshop.objects.all()[0]
    return render(request, 'workshop.html', {'workshop': ws})


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')


@require_POST
def register_view(request):
    if request.is_ajax():
        f = file('/Users/moreka/ce-list.txt')
        found = False

        student_id = request.POST['studentID']
        username = request.POST['username']
        email = request.POST['mail']
        password = request.POST['password']

        needle = student_id + ';' + username

        # check if studentID/CE username exists
        for line in f:
            if line.strip() == needle:
                found = True
                break
        if not found:
            return HttpResponse(u'{ "status": "fail", "message": "اکانت CE یا شماره دانشجویی غیر معتبر است." }')

        # check uniqeness of studentID
        if len(SiteUser.objects.filter(studentID=student_id)) > 0:
            return HttpResponse(u'{ "status": "fail", "message": "شماره دانشجویی معتبر نیست یا قبلا استفاده شده است." }')

        try:
            user = User.objects.create_user(username, email, password)
            user.save()

            siteuser = SiteUser()
            siteuser.studentID = student_id
            siteuser.user = user
            siteuser.save()

        except IntegrityError:  # duplicated username
            return HttpResponse(u'{ "status": "fail", "message": "این کاربر قبلا ثبت نام کرده است." }')

        message = u'ثبت نام شما در سایت انجمن علمی دانشکده کامپیوتر با موفقیت انجام شد. لطفاً هر چه سریع‌تر نسبت به تکمیل اطلاعات کاربری (پروفایل) خود اقدام نمایید. ممنون'
        send_mail(u'ثبت نام در سایت SSC', message, 'm.r.karimi.j@gmail.com', [user.email])

        return HttpResponse(u'{ "status": "success", "message": "ثبت نام موفقیت‌آمیز بود.<br> اکنون می‌توانید با این اکانت وارد شوید." }')

    return HttpResponse('Bad request!')


@require_POST
def login_view(request):
    if request.is_ajax():
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print user, ',And,', username, password
        if user is None:
            return HttpResponse(u'{ "status": "fail", "message": "اطلاعات صحیح نیست." }')

        login(request, user)
        return HttpResponse(u'{ "status": "success", "message": "خوش آمدید" }')