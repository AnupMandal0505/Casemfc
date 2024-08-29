from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
# Create your views here.

def signin(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        print(email)
        print(password)
        try:
            users=User.objects.get(username=email)  
            
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Check Password !')
                return redirect('signin')
        except:
            return redirect('home')
    else:
        return render(request,'auth/signin.html')


@login_required(login_url='signin')
def signout(request):
    logout(request)
    # messages.info(request, "Three credits remain in your account.")
    return redirect('home')