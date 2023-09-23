"""parakh_exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from exam import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Welcome, name='welcome'),
    path('adminlogin/', views.LoginAdmin, name='admin_login'),
    path('studentpage/',views.StudentPage, name='student_page'),
    path('studentpage/studentlogin/', views.StudentLogin, name='student_login'),
    path('studentpage/studentsignup/', views.StudentSignup, name='student_signup'),
    path('studentpage/studentlogin/forgot', views.ForgotDetails, name='forgot_credentials'),
    path('logout/', views.StudentLogout, name='student_logout'),
    path('logout/', views.AdminLogout, name='admin_logout'),
    path('studentboard/', views.StudentBoard, name='student_board'),
    path('studentboard/performance', views.StudPerformanceAnalysis, name='student_performance_analysis'),
    path('studentboard/report', views.StudReport, name='student_report'),
    path('studentboard/account', views.StudAccount, name='student_account'),

    path('adminboard/', views.AdminBoard, name='admin_board'),
]
