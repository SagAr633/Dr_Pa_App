from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    option = (
        ('Doctor', 'Doctor'),
        ('Patient', 'Patient')
    )
    role = models.CharField(choices=option, max_length=10, null=False)
    pro_pic = models.ImageField(upload_to='images', default='default.svg')
    address = models.CharField(max_length=50, null=False)
    line1 = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)
    pin_code = models.CharField(max_length=6, null=False)

    def __str__(self):
        return self.username

    @property
    def is_Doctor(self):
        return self.role == 'Doctor'

    def is_Patient(self):
        return self.role == 'Patient'
