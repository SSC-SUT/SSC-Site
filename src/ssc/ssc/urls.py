from django.conf.urls import patterns, include, url
import workshop.urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^workshop/', include(workshop.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
