from django.contrib import admin
from workshop.models import *


admin.site.register(Workshop)
admin.site.register(Lecturing)
admin.site.register(Attendance)
admin.site.register(Resource)
admin.site.register(SiteUser)