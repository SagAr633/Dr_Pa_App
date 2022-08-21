from django.urls import path
from Users import views

urlpatterns = [

    path('signup', views.SignUpView.as_view(), name='signup'),
    path('login', views.SignInView.as_view(), name='login'),

]
