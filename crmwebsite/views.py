from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCustomerForm
from .models import customer
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            data = User.objects.get(username=username)
            messages.success(request, f"Welcome {data.first_name}, you have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error, you login attempt was failed, Please try again!...")
            return redirect('home')
    else:
        data = customer.objects.all()
        return render (request, 'home.html',{'data':data})

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # User details saved in User model.
            form.save()
            #Authenticate
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            firstname = form.cleaned_data['first_name']
            messages.success(request,f"Welcome {firstname}, you have successfully registered.")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    
    return render(request,'register.html',{'form':form})

def view_customer(request, pk):
    if request.user.is_authenticated:
        data = customer.objects.get(id=pk)
        return render(request,'view.html',{'data':data})
    else:
        messages.success(request,f"Please login and try again!!!")
        return redirect('home')

def delete_customer(request,pk):
    if request.user.is_authenticated:
        data = customer.objects.get(id=pk)
        data.delete()
        messages.success(request,f"Record has been deleted successfully.")
        return redirect('home')
    else:
        messages.success(request,f"Please login and try again!!!")
        return redirect('home')

def add_customer(request):
    if request.user.is_authenticated:
        form = AddCustomerForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request,"Record added successfully.")
                return redirect('home')
        else:
            return render(request,'add.html',{'form':form})
    else:
        messages.success(request,f"Please login and try again!!!")
        return redirect('home')

def update_customer(request,pk):
    if request.user.is_authenticated:
        data = customer.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None,instance=data)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request,"Record has been updated successfully.")
                return render(request,'view.html',{'data':data})
        return render(request, 'update.html',{'form':form,'data':data})
    else:
        messages.success(request,f"Please login and try again!!!")
        return redirect('home')