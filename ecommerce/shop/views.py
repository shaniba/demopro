from django.shortcuts import render,redirect
from django.views import View
from shop.models import Category,Products

from unicodedata import category


# Create your views here.
class CategoryView(View):
    def get(self,request):
        c= Category.objects.all()
        return render(request, 'categories.html',{'Category':c})

class ProductsView(View):
    def get(self,request,i):
        c=Category.objects.get(id=i)
        return render(request, 'products.html', {'category':c})

class DetailView(View):
    def get(self,request,i):
        p=Products.objects.get(id=i)
        return render(request, 'detail.html', {'product':p})

class AddCategoryView(View):
    def get(self,request):
        form_instance = CategoryForm()
        return render(request, 'addcategory.html', {'form':form_instance})
    def post(self,request):
        form_instance = CategoryForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:categories')

class AddProductionView(View):
    def get(self,request):
        form_instance = ProductForm(request.POST,request.FILES)
        return render(request, 'addcategory.html', {'form':form_instance})

    def post(self, request):
        form_instance = ProductForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:categories')

from shop.forms import SignupForm

class SignupView(View):

   def POST(self,request):
       form_instance = SignupForm(request.POST)
       if form_instance.is_valid():
           user = form_instance.save(commit=False)
           user.is_active= False
           # user.set_password(form_instance.cleaned_data['password'])
           user.save()
           user.generate_otp()
           return redirect('shop:otp_verify')



   def get(self,request):
       form_instance= SignupForm()
       return render(request, 'signup.html', {'form': form_instance})

from shop.models import  CustomUser
from django.contrib import messages
class OtpVerificationView(View):
    def post(self,request):
        otp = request.POST.get('otp')
        print(otp)
        try:
           u= CustomUser.objects.get(otp=otp)
           u.is_active =True
           u.is_verified=True
           u.otp=None
           u.save()
           return redirect('shop:categories')
        except:
            messages.error(request, message='invalid otp')
            return redirect('shop:otp_verify')

    def get(self,request):
        return render(request, 'otp_verify.html')

from shop.forms import LoginForm

from django.contrib.auth import authenticate,login,logout

class LoginView(View):
    def post(self, request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            name=form_instance.cleaned_data['username']
            pwd= form_instance.cleaned_data['password']
            print(name,pwd)
            user = authenticate(username=name,password=pwd)


            if user:
                login(request,user)
                u=request.user
                print(u.username)
                print(u.email)
                return redirect('shop:categories')
            else:
                 print('invalid user credntials')
                 return redirect('shop:login')


    def get(self,request):
        form_instance = LoginForm()
        return render(request, 'login.html', {'form':form_instance})


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('shop:login')