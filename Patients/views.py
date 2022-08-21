from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth import logout
from Users.decorators import signin_required
from Doctors.models import DoctorBlog
from django.utils.decorators import method_decorator


class Patient_Detail_View(TemplateView):
    template_name = 'patient_dash.html'


@signin_required
def signout(request):
    logout(request)
    return redirect('login')


@method_decorator(signin_required, name='dispatch')
class AllBlogsListView(ListView):
    model = DoctorBlog
    template_name = 'all-blogs.html'
    context_object_name = 'blogs'
    ordering = ['-id']


class MentalHealthView(ListView):
    model = DoctorBlog
    template_name = 'mental-health.html'
    context_object_name = 'topic'


class HeartDiseaseView(ListView):
    model = DoctorBlog
    template_name = 'heart-disease.html'
    context_object_name = 'topic'


class Covid19View(ListView):
    model = DoctorBlog
    template_name = 'covid19.html'
    context_object_name = 'topic'


class ImmunizationView(ListView):
    model = DoctorBlog
    template_name = 'immunization.html'
    context_object_name = 'topic'


class PatientDetailsView(TemplateView):
    template_name = 'patient_details.html'