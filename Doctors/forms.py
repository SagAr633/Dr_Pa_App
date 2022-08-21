from django import forms
from Doctors.models import DoctorBlog


class DoctorBlogForm(forms.ModelForm):
    class Meta:
        model = DoctorBlog
        exclude = ('__all__',)