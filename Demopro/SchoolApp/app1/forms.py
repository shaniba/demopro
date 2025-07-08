from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
           class Meta:
               model=User
               fields = ['username', 'email', 'password1', 'password2']


from app1.models import School

class SchoolForm(forms.ModelForm):
       class Meta:
           model=School
           fields = ['name', 'principal', 'location',]


class LoginForm(forms.Form):
        username = forms.CharField(max_length=100)
        password = forms.CharField(widget=forms.PasswordInput)
