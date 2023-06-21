from django.contrib import admin
from django.urls import path
from HR import views

urlpatterns = [
    path('', views.index,name='home'),
    path('login',views.login,name='login'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('verifystudent',views.verifystudent,name='verifystudent'),
    path('mock',views.mock,name='mock')

]