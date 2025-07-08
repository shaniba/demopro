from django.contrib.auth import authenticate
from django.shortcuts import render,redirect

# Create your views here.
from django.views import View

class HomeView(View):
    def get(self,request):
        return render(request, 'home.html')

from app1.forms import SignUpForm
class SignUpView(View):
    def get(self, request):
        form_instance = SignUpForm()
        return render(request, 'register.html', {'form': form_instance})

    def post(self, request):
        form_instance = SignUpForm(request.POST)
        if form_instance.is_valid():
            user = form_instance.save()  # Automatically saves user if using UserCreationForm
            login(request, user)  # Optional: log user in after signup
            return redirect('studenthome')  # Change to wherever you want to redirect
        return render(request, 'register.html', {'form': form_instance})

from app1.forms import LoginForm
from django.contrib.auth import authenticate,login,logout


class SignInView(View):
    def get(self, request):
        form_instance = LoginForm()
        return render(request, 'login.html', {'form': form_instance})

    def post(self, request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            u = form_instance.cleaned_data['username']
            pwd = form_instance.cleaned_data['password']
            user = authenticate(username=u, password=pwd)

            if user and user.is_superuser==True:
                        login(request, user)
                        return redirect('adminhome')

            elif user and user.is_superuser==False:
                        login(request, user)
                        return redirect('studenthome')
            else:
                # Invalid credentials
                print('invalid credentials')
                return render(request, 'login.html')
        # Either invalid form or credentials; re-render with errors


class AdminHomeView(View):
    def get(self,request):
        return render(request, 'adminhome.html')

class StudentHomeView(View):
    def get(self,request):
        return render(request, 'studenthome.html')

class SignOutView(View):
    def get(self,request):
        logout(request)
        return redirect('signin')

from app1.models import Student
class SchoolDetailView(View):
    def get(self,request,i):
        s=School.objects.get()

