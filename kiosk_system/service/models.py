from django.db import models


class department(models.Model):
    image = models.ImageField(upload_to='department_directory_images/')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, default="Unknown")   # ✅ safe default
    department = models.CharField(max_length=100, default="General") # ✅ safe default

class announcement(models.Model):
    image = models.ImageField(upload_to='announcement_images/', null=True, blank=True)
    title = models.CharField(max_length=100,default="Important Notice")  # ✅ safe default
    heading = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

# Create your models here.

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    bio = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='customer_appointments'
    )
    provider = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='provider_appointments'
    )
    name = models.CharField(max_length=100, default="General")   # new field
    phone_number = models.CharField(max_length=15, default="0000000000") 
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Confirmed', 'Approved'),
            ('Cancelled', 'Cancelled'),
        ],
        default='Pending'
    )

    def __str__(self):
        return f"{self.customer} → {self.provider}"