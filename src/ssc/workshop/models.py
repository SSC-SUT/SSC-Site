from django.db import models
from django.contrib.auth.models import User


class Workshop(models.Model):
    name = models.CharField(max_length=100)
    breif_description = models.TextField()
    full_description = models.TextField()  # In HTML format, incl. schedule, prerequisits, ...
    fee = models.IntegerField(default=0)
    date = models.DateTimeField(null=True)
    length = models.IntegerField(null=True)
    lecturers = models.ManyToManyField(User, through='Lecturing', related_name='lectured_workshops', null=True)
    attendees = models.ManyToManyField(User, through='Attendance', related_name='attended_workshops', null=True)

    def __unicode__(self):
        return self.name


class Attendance(models.Model):
    attendee = models.ForeignKey(User)
    workshop = models.ForeignKey(Workshop)
    date_registered = models.DateTimeField(auto_now=True)
    transaction_number = models.CharField(max_length=10)
    payment = models.IntegerField()
    is_valid = models.BooleanField(default=False)


class Lecturing(models.Model):
    lecturer = models.ForeignKey(User)
    workshop = models.ForeignKey(Workshop)
    payment = models.IntegerField()
    date_determined = models.DateTimeField(auto_now=True)
