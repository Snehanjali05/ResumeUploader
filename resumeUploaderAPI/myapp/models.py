from django.db import models

# Create your models here.
State_Choice = ((
    ('Telangana','Telangana'),
    ('Andhra Pradesh','Andhra pradesh'),
    ('Tamil Nadu','Tamil Nadu'),
))

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(auto_now = False, auto_now_add = False)
    state = models.CharField(choices=State_Choice, max_length=50)
    gender = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    profileimg = models.ImageField(upload_to='images',blank=True)
    document = models.FileField(upload_to='mydocs', blank = True)
