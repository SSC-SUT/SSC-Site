# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class SiteUser(models.Model):
    user = models.OneToOneField(User)
    studentID = models.CharField(max_length=8, unique=True)
    description = models.CharField(max_length=100, default=u'دانشجوی دانشکده‌ی کامپیوتر')

    def __unicode__(self):
        return self.user.username


class Workshop(models.Model):
    name = models.CharField(max_length=100)
    breif_description = models.TextField()
    full_description = models.TextField()  # In HTML format, incl. schedule, prerequisits, ...
    fee = models.IntegerField(default=0)
    date = models.DateTimeField(null=True)
    length = models.IntegerField(null=True)  # in hours
    place = models.CharField(max_length=50, default='')
    lecturers = models.ManyToManyField(User, through='Lecturing', related_name='lectured_workshops', null=True)
    attendees = models.ManyToManyField(User, through='Attendance', related_name='attended_workshops', null=True)
    lunch = models.CharField(max_length=50, default='')
    lunch_fee = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Attendance(models.Model):
    attendee = models.ForeignKey(User)
    workshop = models.ForeignKey(Workshop)
    date_registered = models.DateTimeField(auto_now=True)
    transaction_number = models.CharField(max_length=10)
    payment = models.IntegerField()
    has_lunch = models.BooleanField(default=True)
    is_valid = models.BooleanField(default=False)


class Lecturing(models.Model):
    lecturer = models.ForeignKey(User)
    workshop = models.ForeignKey(Workshop)
    payment = models.IntegerField()
    date_determined = models.DateTimeField(auto_now=True)


class Resource(models.Model):
    name = models.CharField(max_length=50)
    filename = models.CharField(max_length=200)
    is_public = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now=True)
    description = models.TextField()
    workshop = models.ForeignKey(Workshop)

    def __unicode__(self):
        return self.name