from django.http import HttpResponse 
from django.shortcuts import render


from service.models import department
from service.models import announcement

def intro(request):
    return render(request, "intro.html")

def home(request):
    return render(request, 'home.html')

def campus_nav(request):
    return render(request, 'campus_nav.html') 

from django.shortcuts import render
from django.contrib.auth.models import User

def appointment_booking(request):
    available_profiles = User.objects.filter(profile__is_available=True)
    return render(request, 'profile.html', {'profiles': available_profiles})


def department_directory(request):
    DepartmentData = department.objects.all().order_by('id')
    data={'departments': DepartmentData}
    return render(request, 'department_directory.html', data)

def announcement_section(request):
    AnnouncementData = announcement.objects.all().order_by('-id')
    data = {'announcements': AnnouncementData}
    return render(request, 'announcement_section.html', data)

def help_desk(request):
    return render(request, 'help_desk.html')

def about_us(request):
    return render(request, 'about_us.html')


def student_corner(request):
    return render(request, 'student_corner.html')

def pending_appointment(request):
    return render(request, 'pending_appointment.html')







