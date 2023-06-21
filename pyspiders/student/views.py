from django.shortcuts import render,HttpResponse
from student.models import Student_creds
from HR.models import Student_details,Mock
from django.contrib import messages
import random
import os
from twilio.rest import Client

# Create your views here.
def studentlogin(request):
    if request.method=='POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        user=Student_creds.objects.filter(un=un,pw=pw)
        a=Student_creds.objects.all()
        tpno=''
        b=Student_details.objects.all()
        det=''
        for i in a:
            if i.un==un:
                tpno=i.pno
        for j in b:
            if tpno==j.pno:
                det=j
        x=Mock.objects.all()
        mock=''
        for i in x:
            if i.pno==tpno:
                mock=i
        if user.exists:
            # messages.info(request,'logged in successsfully')
            return render(request,'home.html',{'mock':mock,'det':det})
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'studentlogin.html')
    else:
        return render(request,'studentlogin.html')
def register(request):
    if request.method=='POST':
        pno=request.POST.get('pno')
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        cpw=request.POST.get('cpw')
        std=Student_details.objects.filter(pno=pno)
        unv=Student_creds.objects.filter(pno=pno,un=un)
        if pw==cpw:
            if std.exists():
                if unv.exists():
                    messages.info(request,'Student already exists')
                    return render(request,'register.html')
                else:
                    obj=Student_creds(un=un,pw=pw,pno=pno)
                    obj.save()
                    return render(request,'studentlogin.html')
            else:
                messages.info(request,'Student does not exists')
                return render(request,'register.html')
        else:
            messages.info(request,'Password does not match')
            return render(request,'register.html')

    else:
        return render(request,'register.html')
    
def home(request):
    return render(request,'home.html')

def OTP():
    a=random.randint(100000,999999)
    return (a)

x=OTP()

def forgotpwd(request):
    if request.method=='POST':
        pno=request.POST.get('pno')
        pnov=Student_creds.objects.filter(pno=pno)
        if pnov.exists():
            account_sid = "ACe0731ca4fb8eb26abb554ad7bd1229d4"
            auth_token = "bca879a69c319a8dfc341e166e5e5287"
            client = Client(account_sid, auth_token)
            message = client.messages.create(
            body=("Hello mrunali here this is your otp to login :"+str(x)+"please dont share with anyone"),
            from_="+14066257990",
            to="+91"+pno
            )
            messages.info(request,'OTP sent successfully')
            return render(request,'otp.html')
        else:
            messages.info(request,'OTP sent successfully')
            return render(request,'forgotpwd.html')
    else:
        return render(request,'forgotpwd.html')
    
def otp(request):
    if request.method=='POST':
        otp=request.POST.get('enterotp')
        if otp==str(x):
            messages.info(request,'OTP verified successfully')
            return render(request,'resetpassword.html')
        else:
            messages.info(request,'Invalid OTP')
            return render(request,'otp.html')
        
def resetpassword(request):
    if request.method=='POST':
        pno=request.POST.get('pno')
        # pw=request.POST.get('pw')
        # un=request.POST.get('un')
        newpwd=request.POST.get('newpwd')
        cnewpwd=request.POST.get('cnewpwd')
        rpwv=Student_creds.objects.filter(pno=pno)
        if rpwv.exists:
            if newpwd==cnewpwd:
                rpwv.update(pw=newpwd)
                messages.info(request,'Password Updated Successfully')
                return render(request,'studentlogin.html')
            else:
                messages.info(request,'new password and conformed password does not match')
                return render(request,'resetpassword.html')
        else:
            messages.info(request,'Student Phone Number Does Not exists')
            return render(request,'resetpassword.html')
    else:
        return render(request,'resetpassword.html')