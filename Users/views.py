from django.shortcuts import render, redirect
from Users.models import User
from Users.forms import SignUpForm, SignInForm
from django.views.generic import CreateView, FormView, TemplateView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class SignInView(FormView):
    model = User
    form_class = SignInForm
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if not user:
                return render(request, 'login.html', {'form': form})
            login(request, user)
            if request.user.is_Doctor:
                return redirect('dr_dash')
            else:
                return redirect('pat_dash')