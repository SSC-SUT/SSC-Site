from django.conf.urls import patterns, include, url
import workshop.urls
import workshop.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^workshop/', include(workshop.urls)),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^logout$', workshop.views.logout_view),
    url(r'^register_site$', workshop.views.register_view),
    url(r'^login_site$', workshop.views.login_view),
)
