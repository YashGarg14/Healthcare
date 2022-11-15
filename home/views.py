from home.models import Contact
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4 or phone.isnumeric()==False:
            messages.error(request, "Please enter phone number correctly")
        if name.isalpha()==False:
            messages.error(request, "Please enter name correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")

def home(request):
    return render(request, 'home/home.html')

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']


        # check for errorneous input
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('signup')
        if len(pass1)<8:
             messages.error(request, "Password length must be atleast 8 characters")
             return redirect('signup')

        else:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname

            myuser.save()

            messages.success(request,"Your Account has been created successfully")
            return redirect("signin")

    return render(request, 'home/signup.html')

def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request,"You have been logged in successfully")
            return render(request, 'home/home.html', {'username':username})

        else:
            messages.error(request, "Invalid Credentials")
            return redirect('signin')

    return render(request, 'home/login.html')

def signout(request):
    logout(request)
    # messages.success(request,"Logout successfully")
    return redirect("home")

def about(request):
    pass

def consultation(request):
    # if not request.user.is_authenticated:
    #     return redirect('signin')
    # else:
    return render(request, 'home/consultation.html')

def ambulance(request):
    return render(request, 'home/call_ambulance.html')

def AR_tut(request):
    return render(request, 'home/AR_tut.html')