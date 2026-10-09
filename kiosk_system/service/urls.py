from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
    path('availability/', views.toggle_availability, name='toggle_availability'),
    path('book/<str:username>/', views.book_appointment, name='book_appointment'),
    path("appointment/pending/", views.pending_appointment, name="pending_appointment"),
    path("faculty_profile/<str:username>/", views.faculty_profile, name="faculty_profile"),
     path("update_appointment_status/<int:appointment_id>/", views.update_appointment_status, name="update_appointment_status"),

    path("faculty-login/", views.faculty_login, name="faculty_login"),
]
