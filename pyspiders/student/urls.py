from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('studentlogin',views.studentlogin,name='studentlogin'),
    path('register',views.register,name='register'),
    path('home',views.home,name='home'),
    path('forgotpwd',views.forgotpwd,name='forgotpwd'),
    path('otp',views.otp,name='otp'),
    path('resetpassword',views.resetpassword,name='resetpassword')

]