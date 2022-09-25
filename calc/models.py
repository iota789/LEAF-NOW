from asyncio.windows_events import NULL
from enum import unique
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id= models.EmailField(max_length=20)
    phone_no=PhoneNumberField(unique=True,blank=False)
    address=models.CharField(max_length=50)
    pdet=models.CharField(max_length=50)
    payment=models.CharField(max_length=15)
    d_id=models.BooleanField(default=False)
    s_id=models.BooleanField(default=False)
    