from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
def Test_case1(request):
    return render(request,"Mainpage.html")
def Test_case2(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('Main')
        else:
            return HttpResponse("Username or Password is incorrect......")
    return render(request,"Signin.html")
def Test_case3(request):
    if request.method=='POST':
        Fullname=request.POST.get('Name')
        Mobilenumber=request.POST.get('Mobilenumber') 
        Emailid=request.POST.get('Email') 
        Username=request.POST.get('username')
        Password=request.POST.get('Password')    
        Confirmpassword=request.POST.get('Confirmpassword')
        if Password!=Confirmpassword:
            return HttpResponse("Your password and confirmpassword are not same.......")
        else:
            My_user=User.objects.create_user(Username,Emailid,Password)
            My_user.save()
            return redirect('Sign')       
    return render(request,"Sign up.html")
def Test_case4(request):
    return render (request,"menu.html")
    
