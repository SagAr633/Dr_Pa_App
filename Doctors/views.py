from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, CreateView, ListView
from django.contrib.auth import logout
from Users.decorators import signin_required
from Doctors.models import DoctorBlog
from Doctors.forms import DoctorBlogForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.text import Truncator


class DoctorDashView(TemplateView):
    template_name = 'doctor_dash.html'


@signin_required
def signout(request):
    logout(request)
    return redirect('login')


@method_decorator(signin_required, name='dispatch')
class DoctorBlogView(CreateView):
    model = DoctorBlog
    form_class = DoctorBlogForm
    template_name = 'post_blog.html'
    success_url = reverse_lazy('user_blogs')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(signin_required, name='dispatch')
class DoctorBlogsListView(ListView):
    model = DoctorBlog
    template_name = 'user_blogs.html'
    context_object_name = 'blogs'
    ordering = ['-id']

    # def get_queryset(self):
    #     return DoctorBlog.objects.filter(author=self.request.user)


class DoctorDetailsView(TemplateView):
    template_name = 'doc_details.html'
