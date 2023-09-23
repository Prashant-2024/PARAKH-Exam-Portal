from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def Welcome(request):
    return render(request, 'welcome.html')





def StudentPage(request):
    return render(request, 'student_page.html')

def StudentSignup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1!=pass2:
            return HttpResponse("Your Password and Confirm Password are not same")
        else:
            my_user=User.objects.create_user(uname, email, pass1)
            # return HttpResponse("User has been Created Successfully.")
            my_user.save()
            return redirect('student_login')
            

            # print(uname, firstname, lastname, email, pass1, pass2)

    return render(request, 'student_signup.html')

def StudentLogin(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request, username=uname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('student_board')

    return render(request, 'student_signin.html')

def ForgotDetails(request):
    return render(request, 'forgot_credentials.html')

def LoginAdmin(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request, username=uname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('admin_board')
    return render(request, 'admin_login.html')

def StudentBoard(request):
    pass

def AdminBoard(request):
    return render(request, 'admin_board.html')