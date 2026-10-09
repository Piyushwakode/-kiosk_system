from django.contrib import admin
from service.models import department
from service.models import announcement

from .models import Profile, Appointment

from django.contrib.admin import AdminSite

class CseAdminSite(AdminSite):

    site_header = ' CSE FACULTY ADMIN'
    site_title = ' CSE FACULTY ADMIN PORTAL'
    index_title = 'WELCOME TO CSE FACULTY PORTAL'

cse_admin_site =  CseAdminSite(name = 'cse_admin')


cse_admin_site.register(announcement)


class AimlAdminSite(AdminSite):

    site_header = ' AIML Faculty Admin'
    site_title = ' AIML Faculty Admin Portal'
    index_title = 'WELCOME TO AIML FACULTY PORTAL'

aiml_admin_site =  AimlAdminSite(name = 'aiml_admin')

aiml_admin_site.register(announcement)






admin.site.site_header = "JIT  Administration"
admin.site.site_title = "JIT Admin Portal"
admin.site.index_title = "Welcome to JIT Admin"

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('image','name','position', 'department',)

admin.site.register(department, DepartmentAdmin)

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'heading', 'description', 'date')

admin.site.register(announcement, AnnouncementAdmin)







@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_available')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'provider',
        'name',
        'phone_number',
        'date',
        'time',
        'status'
    )

    list_filter = ('status', 'date')