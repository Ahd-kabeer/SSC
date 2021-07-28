from django.shortcuts import render,redirect
from django.http import HttpResponse
from SC_app.models import *
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout,login


# Create your views here.

def index(request):
    return render(request,'index.html')
def signup(request):
    if request.method == 'POST':
        Fname=request.POST.get('fname')
        Lname= request.POST.get('lname')
        uname = request.POST.get('uname')
        
        email = request.POST.get('email')
        pword = request.POST.get('pword')
        cpword = request.POST.get('cpword')
        if pword == cpword:
            if uname == User.username:
                messages.warning(request,"username already exists,try another one")
                return render(request,'signup.html')
            User.objects.create_user(first_name=Fname,last_name=Lname,username=uname,email = email,password=pword)
            
            return redirect('signin')
        
        else:
            messages.warning(request,"check your password and try again")
            return render(request,"signup.html")
    return render(request,"signup.html")

def signin(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pword = request.POST.get('pword')
        user = authenticate(request,username=uname,password=pword)
        if user is None:
            messages.warning(request,"check your Credentials and try again")
            return render(request,"signin.html")
        else:
            return redirect('index')
    return render(request,"signin.html")

def signout(request):
    auth.logout(request)
    return redirect('signin')



def Book_rooms(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        address = request.POST.get('address')
        mob = request.POST.get('mob')
        ch_in = request.POST.get('checkin')
        ch_out = request.POST.get('checkout')
        NOV = request.POST.get('NOV')
        BT = request.POST.get('BT')

        sc= Booking.objects.create(First_name=fname,Last_name=lname,Address=address,Phone_no=mob,Check_in=ch_in,Check_out=ch_out,Number_of_visitors=NOV,Bed_type=BT)
        sc.save()
        messages.warning(request,"Booking completed successfully!")
        return redirect('index')
    return render(request,'form.html')

    