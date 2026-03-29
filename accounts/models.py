from django.db import models
from django.contrib.auth.models import AbstractUser
import re


class CustomUser(AbstractUser):
    phone = models.CharField(max_length = 20, blank = True, null = True)


class Profile(models.Model):

    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    matric_no = models.CharField(max_length=12) # change this to a custom field
    bio = models.CharField(max_length=512)
    avatar = models.ImageField(upload_to = "media/accounts") # external uploads for prod.
    dept = models.CharField(max_length = 64, default = "Computer Science")

    def save(self,*args,**kwargs):
        if re.match(r"^CSC/\d{2}/\d{4}$", self.matric_no):
            super().save(args, kwargs)
        else:
            raise ValueError

