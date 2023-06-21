from django.shortcuts import render,HttpResponse
from HR.models import Creds,Student_details,Mock
from django.contrib import messages
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        un=request.POST.get('username')
        pw=request.POST.get('password')
        user=Creds.objects.all()
        a=False
        unv=False
        pwv=False
        for i in user:
            if i.username==un:
                unv=True
                if i.password==pw:
                    pwv=True
                    a=True
        if unv==True:
            if pwv==True:
                return render(request,'index.html',{'a':a})
            else:
                messages.info(request,'Invalid Password')
                return render(request,'login.html')
        else:
            messages.info(request,'Invalid Username')
            return render(request,'login.html')
            
            
    else:
        return render(request,'login.html')
    
def addstudent(request):
    if request.method=='POST':
        name=request.POST.get('sname')
        pno=request.POST.get('pno')
        email=request.POST.get('email')
        qual=request.POST.get('qual')
        stream=request.POST.get('str')
        dyop=request.POST.get('dyop')
        dp=request.POST.get('dp')
        twp=request.POST.get('twp')
        tp=request.POST.get('tp')
        user=Student_details.objects.filter(pno=pno,email=email)
        if user.exists():
            messages.info(request,'Student is already Registerd')
            return render(request,'addstudent.html')
        else:
            addstd=Student_details(name=name,pno=pno,email=email,qual=qual,stream=stream,dyop=dyop,dp=dp,twp=twp,tp=tp)
            addstd.save()
            return render(request,'verifystudent.html')
    return render(request,'addstudent.html')

def verifystudent(request):
    if request.method=='POST':
        pno=request.POST.get('pno')
        email=request.POST.get('email')
        objects=Student_details.objects.all()
        std=''
        for i in objects:
            if i.pno==pno or i.email==email:
                std=i
                return render(request,'verifystudent.html',{'std':std})

    return render(request,'verifystudent.html')

def mock(request):
    if request.method=='POST':
        name=request.POST.get('nme')
        pno=request.POST.get('pno')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        comm=request.POST.get('comm')
        tech=request.POST.get('tech')
        prog=request.POST.get('prog')
        Trainers=request.POST.get('Trainers')
        mock1=Mock.objects.filter(pno=pno,subject=subject)
        if mock1.exists():
            mock1.update(comm=comm,tech=tech,prog=prog,by=Trainers,date=datetime.today())
            messages.info(request,'Mock ratings updated successfully')
            return render(request,'mock.html')
        else:
            abc=Mock(name=name,pno=pno,email=email,subject=subject,comm=comm,tech=tech,prog=prog,by=Trainers,date=datetime.today())
            abc.save()
            messages.info(request,'Mock ratings added successfully')
            return render(request,'mock.html')
        
    else:
        return render(request,'mock.html')
    # return render(request,'mock.html')




