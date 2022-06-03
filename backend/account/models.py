from django.db import models

class User(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    fullname = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    gender = models.CharField(choices=GENDER, default='Male', max_length=10)
    username = models.CharField(max_length=100, blank=True)
    active = models.BooleanField(default=False)
    

