
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from service.models import Appointment
from service.models import Profile
from django.contrib.auth import authenticate, login
from django.contrib import messages


def profile(request, username):
    user = get_object_or_404(User, username=username)
    appointments = Appointment.objects.filter(provider=user).order_by('date', 'time')
    return render(request, 'profile.html', {
        'profile_user': user,
        'appointments': appointments
    })

def faculty_profile(request, username):
    user = get_object_or_404(User, username=username)
    appointments = Appointment.objects.filter(provider=user).order_by('date', 'time')
    return render(request, 'faculty_profile.html', {
        'profile_user': user,
        'appointments': appointments
    })



def toggle_availability(request):
    profile = request.user.profile

    if request.method == "POST":
        profile.is_available = not profile.is_available
        profile.save()

    return redirect(
        'profile',
        username=request.user.username
    )


def book_appointment(request, username):
    provider = get_object_or_404(User, username=username)

    if request.method == "POST":
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        date = request.POST.get('date')
        time = request.POST.get('time')

        Appointment.objects.create(
            customer=request.user,
            provider=provider,
            name=name,
            phone_number=phone_number,
            date=date,
            time=time
        )

      
        return redirect('pending_appointment') 

        
    return render(request, 'appointment_booking.html', {
        'provider': provider
    })



def pending_appointment(request):
    appointments = Appointment.objects.filter(customer=request.user, status="Pending")
    return render(request, "pending_appointment.html", {"appointments": appointments})



def faculty_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("faculty_profile", username=user.username)
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "faculty_login.html")


# service/views.py
from django.shortcuts import redirect, get_object_or_404
from .models import Appointment

def update_appointment_status(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == "POST":
        new_status = request.POST.get("status")
        appointment.status = new_status
        appointment.save()
    return redirect("faculty_profile", username=appointment.provider.username)
