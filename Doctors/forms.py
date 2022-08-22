from django import forms
from Doctors.models import DoctorBlog


class DoctorBlogForm(forms.ModelForm):
    class Meta:
        model = DoctorBlog
        fields = [
            'author',
            'category',
            'title',
            'image',
            'summary',
            'content'
        ]