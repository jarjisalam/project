from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def signup(request):

    if request.method=="POST":
        get_email=request.POST.get('email')
        get_password=request.POST.get('password')
        get_confirm_password=request.POST.get('password2')
        if get_password != get_confirm_password:
            messages.info(request,'Password in not matching')
            return redirect('/auth/signup/')
        
        try:
            if User.objects.get(username=get_email):
                messages.warning(request,"Email is taken")
                return redirect('/auth/signup/')
        except Exception as identifier:
            pass
        myuser= User.objects.create_user(get_email,get_email,get_password)
        myuser.save()

        myuser=authenticate(username=get_email,password=get_password)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,'User is Created & login success')
            return redirect('/')
        
    return render(request,'signup.html')

def handleLogin(request):
    if request.method=="POST":
        get_email=request.POST.get('email')
        get_password=request.POST.get('password')
        myuser=authenticate(username=get_email,password=get_password)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,'login success')
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials')
    return render(request,'login.html')

def handleLogout(request):
    logout(request)
    messages.success(request,'logout succss')
    return render(request,'Login.html')

