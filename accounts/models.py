from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import re


class CustomUser(AbstractUser):
    phone = models.CharField(max_length = 20, blank = True, null = True)

class BaseProfile(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='%(class)s_profile')
    avatar = models.ImageField(upload_to = "accounts",null=True,blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"Profile of  {self.user.username}"

class StudentProfile(BaseProfile):
    # This profile is the general student profile
    matric_no = models.CharField(unique=True,max_length=12)
    dept = models.CharField(max_length = 64, default = "Computer Science")
    

    def clean(self):
        if re.match(r"^CSC/\d{2}/\d{4}$", self.matric_no):
            ...
        else:
            raise ValidationError({
                'matric_no': 'This field does not satisfy the pattern CSC/00/0000.'
            })

class FreshmanProfile(BaseProfile):
    # This is a profile for Freshman/fresher
    registration_no = models.CharField(unique=True,max_length=14)
    dept = models.CharField(max_length = 64, default = "Computer Science")

    def clean(self):
        if re.match(r"^\d{4}\d{8}[A-Za-z]{2}$", self.registration_no):
            ...
        else:
            raise ValidationError({
                'registration_no': 'This field does not satisfy the pattern 202512345678AB.'
            })