from django.shortcuts import render

# Create your views here.

def LandingPage(request):
    return render(request, 'landing_page.html')

def HomePage(request):
    pass

def SignupPage(request):
    pass

def LoginPage(request):
    pass