from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from calc.models import Person
from django.forms import ModelForm



class CUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]

class donator(ModelForm):
    
        class Meta:
            model = Person
            fields=["first_name","last_name","email_id","phone_no","address","pdet","payment"]
