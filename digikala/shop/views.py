from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .models import Product, Category
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

def category_summary(request):
   all_cat =Category.objects.all()
   return render(request, 'category_summary.html', {'category':category})


def Firstpage(request):
   all_products = Product.objects.all()
   return render(request, 'index.html', {'products': all_products})


def about(request):
   return render(request, 'about.html')

def login_user(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']

      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request, user)
         messages.success(request, ('باموفقیت وارد شدید') )
         return redirect("home")
      else:
         messages.success(request, ('مشکلی در لاگین وجود داشت'))
         return redirect("login")
   else:
      return render(request, 'login.html')

def logout_user(request):
   logout(request)
   messages.success(request, 'باموفقیت خارج شدید')
   return redirect("home")

def signup_user(request):
   form = SignUpForm()
   if request.method == "POST":
      form = SignUpForm(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data['username']
         password1 = form.cleaned_data['password1']
         user = authenticate(request, username=username, password=password1)
         login(request, user)
         messages.success(request, ('اکانت شما ساخته شد'))
         return redirect("home")
      else:
         messages.success(request, ('مشکلی در ثبتنام شما وجود داشت'))
         return redirect("signup")
   else:
      return render(request, 'signup.html', {'form': form})
   
def product(request,pk):
   product = Product.objects.get(id=pk)
   return render(request, 'product.html', {'product': product})

def category(request,cat):
   cat = cat.replace("-"," ")
   try:
      category = Category.objects.get(name=cat),
      products = Product.objects.filter(category=category),
      return render(request, 'category.html',{'products':products, "category":category})
                                                
   except:  
       messages.error(request, "دسته بندی وجود ندارد.")  
       return redirect('home')