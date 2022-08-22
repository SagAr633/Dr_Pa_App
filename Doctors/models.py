from django.db import models
from Users.models import User
from django.urls import reverse


class DoctorBlog(models.Model):
    options = (
        ('Mental Health', 'Mental Health'),
        ('Heart Disease', 'Heart Disease'),
        ('Covid19', 'Covid19'),
        ('Immunization ', 'Immunization ')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dr_author')
    category = models.CharField(max_length=30, choices=options, null=False, blank=False)
    title = models.CharField(max_length=500, null=False, blank=False)
    image = models.ImageField(upload_to='blog_images')
    summary = models.CharField(max_length=500, null=False, blank=False)
    content = models.CharField(max_length=3000, null=False, blank=False)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('user_blogs')



