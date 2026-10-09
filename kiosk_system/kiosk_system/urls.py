"""
URL configuration for kiosk_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from kiosk_system import views  
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from service.admin import cse_admin_site
from service.admin import aiml_admin_site


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cse-admin/',cse_admin_site.urls),
    path('aiml-admin/',aiml_admin_site.urls),
    path('', views.intro, name='intro'),
    path('home/', views.home, name='home'),
    path('campus_nav/', views.campus_nav, name='campus_nav'),
    path('appointment_booking/', views.appointment_booking, name='appointment_booking'),
    path('department_directory/', views.department_directory, name='department_directory'),
    path('announcement_section/', views.announcement_section, name='announcement_section'),
    path('help_desk/', views.help_desk, name='help_desk'),
    path('about_us/', views.about_us, name='about_us'),
    path('pending_appointment/', views.pending_appointment, name='pending_appointment'),
    path('student_corner/', views.student_corner, name='student_corner'),
    path('i18n/', include('django.conf.urls.i18n')),  # language switcher
    path('', include('service.urls')),


    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)