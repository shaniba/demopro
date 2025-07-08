from django import forms
from django.contrib.auth.forms import UserCreationForm
from shop.models import CustomUser

class SignupForm(UserCreationForm):
 class Meta:
      model=CustomUser
      fields =['username','password1','password2','email','first_name','last_name','phone']



class LoginForm(forms.Form):

      username = forms.CharField()
      password = forms.CharField(widget=forms.PasswordInput)