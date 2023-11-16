from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def login_page(request):
    if request.method == 'POST':
        
        email = request.POST['username']
        passw = request.POST['passw']
        print(request.POST)
        
        user =  User.objects.filter(username = email)

        if not user.exists():
            messages.warning(request, "Account does not exist")
            return HttpResponseRedirect(request.path_info)
        
        if not user[0].profile.is_email_verified:
            messages.warning(request, "Please verify your account first")
            return HttpResponseRedirect(request.path_info)



        user = authenticate(username = email, password = passw)

        if user:
            login(request, user)
            return redirect('login')
        

        messages.warning(request, "Invalid Credentials")
        return HttpResponseRedirect(request.path_info)
    

    return render(request,'accounts/login.html')

    



        
    return render(request, "accounts/register.html")

def signup_page(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        passw = request.POST['passw']
        cpass = request.POST['cpass']

        print(request.POST)
        user =  User.objects.filter(username = email)
        if user.exists():
            messages.warning(request, "Email is already taken!")
            return HttpResponseRedirect(request.path_info)
        
        user = User.objects.create_user(first_name = first_name, last_name = last_name, email = email, username = email)
        user.set_password(passw)
        user.save()

        messages.success(request, "An email has been sent on your mail")
        return HttpResponseRedirect(request.path_info)
    

    return render(request,'accounts/register.html')

    



        
    return render(request, "accounts/register.html")