from django.shortcuts import render

# Create your views here.

def Welcome(request):
    return render(request, 'welcome.html')

def StudentBoard(request):
    pass

def AdminBoard(request):
    pass

def StudentPage(request):
    return render(request, 'student_page.html')

def StudentSignup(request):
    return render(request, 'student_signup.html')

def StudentLogin(request):
    return render(request, 'student_signin.html')

def ForgotDetails(request):
    return render(request, 'forgot_credentials.html')

def LoginAdmin(request):
    return render(request, 'admin_login.html')